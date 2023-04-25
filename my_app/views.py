from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import View
from .models import Member, all_models
from datetime import date
from .forms import UserCreationForm, MemberWorkDayForm
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.forms import modelformset_factory

tables_names = [i.__name__ for i in all_models]

def table_view(request, table_name):
    model = apps.get_model(app_label='my_app', model_name=table_name)
    model_fields = model._meta.fields
    model_field_names = [f.name for f in model_fields if
                         not isinstance(f, models.ManyToOneRel) and f.name != 'id']

    # Create a formset for the model
    formset_factory = modelformset_factory(model, fields=model_field_names)
    formset = formset_factory(queryset=model.objects.all())

    context = {
        'table_name': table_name,
        'formset': formset,  # Add formset to context
        'model_field_names': model_field_names,
    }

    if request.method == 'POST':
        formset = formset_factory(request.POST, queryset=model.objects.all())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in formset.deleted_objects:
                instance.delete()
            formset.save()  # сохраняем изменения в базе данных

    return render(request, 'my_app/table.html', context)



def create_view(request, table_name):
    if table_name not in tables_names:
        return render(request, 'my_app/tables/none.html')

    model = apps.get_model('my_app', table_name)
    field_names = [f.name for f in model._meta.get_fields() if f.editable and not f.is_relation and not f.name == 'id']

    if request.method == 'POST':
        model.objects.create(**{f: request.POST[f] for f in field_names})
        return redirect('table_view', table_name=table_name)

    context = {'table_name': table_name,
               'field_names': field_names}

    return render(request, 'my_app/create.html', context)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.get_user()
        self.success_url = reverse_lazy(f'{user.role.role}-table')
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url


@login_required
@user_passes_test(lambda u: u.role.role == 'admin')
def admin_table(request):
    return render(request, 'my_app/admin_table.html', {'models': tables_names})


@login_required
@user_passes_test(lambda u: u.role.role == 'accountant')
def accountant_table(request):
    return render(request, 'my_app/accountant_table.html')


@login_required
@user_passes_test(lambda u: u.role.role == 'security')
def security_table(request):
    return render(request, 'my_app/security_table.html')


def current_month(request):
    days = range(date.today().day - 3, date.today().day + 1)
    guys = Member.objects.filter(is_actual=True)
    form = MemberWorkDayForm()
    return render(request, 'my_app/days.html', context={'members': guys, 'days': days, 'form': form})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
