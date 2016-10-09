from django import forms
from django.contrib.auth.models import User

from .models import TJob


class DateInput(forms.DateInput):
    input_type = 'date'


class TJobForm(forms.ModelForm):
    companyName = forms.CharField(label="Company Name: ", max_length=50,
                                  widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    appliedOn = forms.DateField(label="Applied On: ", widget=DateInput(attrs={'class': 'form-control'}))
    source = forms.CharField(label="Source: ", max_length=50,
                             widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    jobId = forms.CharField(label="Job ID: ", max_length=50,
                            widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    jobDesc = forms.CharField(label="Job Description: ", max_length=200,
                              widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    statusLink = forms.URLField(label="Status link: ", max_length=200,
                                widget=forms.widgets.Input(attrs={'class': 'form-control'}))

    myChoice = (
        ('A', 'Accept'),
        ('R', "Reject"),
        ('U', "Unknown")
    )
    result = forms.ChoiceField(label="Result: ", choices=myChoice, widget=forms.Select(attrs={'class': 'form-control'}))
    user = None

    class Meta:
        model = TJob
        fields = ['companyName', 'appliedOn', 'source', 'jobId', 'jobDesc',
                  'statusLink', 'result', 'user']
        widgets = {
            'appliedOn': DateInput(),
        }


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.widgets.Input(
        attrs={'class': 'form-username form-control', 'placeholder': 'Username', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-password form-control', 'placeholder': 'Password', 'autocomplete': 'off'}))
    email = forms.CharField(widget=forms.widgets.Input(
        attrs={'class': 'form-email form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        # class UserProfileForm(forms.ModelForm):
        #     class Meta:
        #         model = UserProfile
        #         fields = ('website', 'picture')
