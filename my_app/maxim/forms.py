from django import forms
from .models import Data

from datetime import timedelta


class MemberWorkDayForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('member', 'start_time', 'end_time', 'project', 'lunch_break')
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'lunch_break': forms.Select(choices=[
                (timedelta(minutes=15), '15 минут'),
                (timedelta(minutes=30), '30 минут'),
                (timedelta(minutes=45), '45 минут'),
                (timedelta(minutes=60), '1 час'),
            ]),
        }