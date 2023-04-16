from django.shortcuts import render
from django.views.generic import FormView
from .forms import MemberWorkDayForm
from .models import Member

from datetime import date


# def members(request):
#     guys = Member.objects.all()
#     return render(request, 'employees/members.html', context={'guys': guys})


def current_month(request):
    days = range(date.today().day - 3, date.today().day + 1)
    guys = Member.objects.filter(is_actual=True)
    form = MemberWorkDayForm()
    return render(request, 'employees/days.html', context={'members': guys, 'days': days, 'form': form})

# class DaysView(FormView):
#     form_class = MemberWorkDayForm
#     template_name = 'employees/days.html'
# success_url = '/done'
