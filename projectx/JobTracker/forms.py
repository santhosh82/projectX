from django import forms
from django.contrib.auth.models import User

from .models import TJob


class TJobForm(forms.ModelForm):

    companyName = forms.CharField(label="Company Name: ", max_length=50,
                                  widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    appliedOn = forms.DateField(label="Applied On: ", widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    source = forms.CharField(label="Source: ", max_length=50,
                             widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    jobId = forms.CharField(label="Job ID: ", max_length=50,
                            widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    jobDesc = forms.CharField(label="Job Description: ", max_length=200,
                              widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    statusLink = forms.URLField(label="Status link: ", max_length=200,
                                widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    ACCEPT = "A"
    REJECT = "R"
    UNKNOWN = "U"
    myChoice = (
        (ACCEPT, 'accept'),
        (REJECT, "reject"),
        (UNKNOWN, "unknown")

    )

    result = forms.CharField(label="Result: ", max_length=1,
                             widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    user = None

    class Meta:
        model = TJob
        fields = ['companyName', 'appliedOn', 'source', 'jobId', 'jobDesc',
                  'statusLink', 'result']
        exclude = ['user']


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.widgets.Input(attrs = {'class' : 'form-username form-control','placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class' : 'form-password form-control','placeholder':'password'}))
    email = forms.CharField(widget=forms.widgets.Input(attrs = {'class' : 'form-email form-control','placeholder':'email'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        # class UserProfileForm(forms.ModelForm):
        #     class Meta:
        #         model = UserProfile
        #         fields = ('website', 'picture')
