from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.apps import apps
from django.views.generic import UpdateView, ListView
from .models import Member, all_models
from datetime import date
from .forms import UserCreationForm, MemberWorkDayForm


# class ModelList(ListView):
#     model = None
#     template_name = 'model_list.html'
#
#     def get_queryset(self):
#         model_name = self.kwargs['model_name']
#         self.model = apps.get_model('app_name', model_name)
#         return self.model.objects.all()
#
#
# class ModelEdit(UpdateView):
#     model = None
#     template_name = 'model_edit.html'
#     fields = '__all__'
#
#     def get_object(self):
#         model_name = self.kwargs['model_name']
#         self.model = apps.get_model('app_name', model_name)
#         pk = self.kwargs['pk']
#         return self.model.objects.get(pk=pk)
#
#     def get_success_url(self):
#         return reverse('model_list', args=[self.model._meta.model_name])


tables_names = [i.__name__ for i in all_models]


def table_view(request, table_name):
    if table_name not in tables_names:
        return render(request, 'my_app/tables/none.html')
    return render(request, f'my_app/tables/{table_name.lower()}.html', {'table': tables_names})


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
