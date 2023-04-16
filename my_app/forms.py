from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Data

from datetime import timedelta


User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


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