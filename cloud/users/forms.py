from django import forms
from django.utils.translation import gettext_lazy as _

from allauth.account.forms import SignupForm
from django_countries import countries

from .models import Student, User
from .choices import ROLE_CHOICES

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Name')
    }), max_length=255, label=_('First Name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Last Name')
    }), max_length=255, label=_('Last Name'))
    country = forms.ChoiceField(widget=forms.Select(), choices=countries, label=_('Country'))

    role = forms.ChoiceField(widget=forms.Select(attrs={
        'id': 'role'
    }), choices=ROLE_CHOICES, label=_('Client Type'))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+1987654321'
    }), max_length=24, label=_('Phone'), required=False)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'style': 'width: 33%; display: inline-block'
    }, years=range(2021, 1920, -1)), label=_('Date of birth'), required=False)
    school = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('School')
    }), max_length=255, label=_('School'), required=False)

    def save(self, request):
        user: User = super(CustomSignupForm, self).save(request)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.country = self.cleaned_data.get('country')
        user.role = int(self.cleaned_data.get('role'))

        if int(user.role) == 1:
            # user.document = self.cleaned_data.get('document')
            user.phone = self.cleaned_data.get('phone')

        if int(user.role) == 2:
            # user.document = self.cleaned_data.get('document')
            user.phone = self.cleaned_data.get('phone')
            user.school = self.cleaned_data.get('school')

        if int(user.role) == 3:
            # user.document = self.cleaned_data.get('document')
            user.phone = self.cleaned_data.get('phone')
            user.date_of_birth = self.cleaned_data.get('date_of_birth')
            user.school = self.cleaned_data.get('school')
            
        user.save()
        return user


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'school']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        student = super().save(commit=False)
        student.parent = self.request.user
        student.save()
        return student


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Name')
    }), max_length=255, label=_('First Name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Last Name')
    }), max_length=255, label=_('Last Name'))
    country = forms.ChoiceField(widget=forms.Select(), choices=countries, label=_('Country'))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+1987654321'
    }), max_length=24, label=_('Phone'), required=False)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'style': 'width: 33%; display: inline-block'
    }, years=range(2021, 1920, -1)), label=_('Date of birth'), required=False)
    school = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('School')
    }), max_length=255, label=_('School'), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'country', 'phone', 'date_of_birth', 'school']

    def save(self, commit=True):
        user: User = super().save(commit=False)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.country = self.cleaned_data.get('country')

        if int(user.role) == 1:
            # user.document = self.cleaned_data.get('document')
            user.phone = self.cleaned_data.get('phone')

        if int(user.role) == 2:
            # user.document = self.cleaned_data.get('document')
            user.phone = self.cleaned_data.get('phone')
            user.school = self.cleaned_data.get('school')

        if int(user.role) == 3:
            # user.document = self.cleaned_data.get('document')
            user.phone = self.cleaned_data.get('phone')
            user.date_of_birth = self.cleaned_data.get('date_of_birth')
            user.school = self.cleaned_data.get('school')
            
        user.save()
        return user