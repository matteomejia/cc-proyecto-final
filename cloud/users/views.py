from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView, TemplateView, CreateView

from cloud.store.models import Inscription

from .forms import StudentForm, UserForm
from .models import User, Student
# Create your views here.

class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.filter(parent=self.request.user)
        context['inscriptions'] = Inscription.objects.filter(user=self.request.user, paid=True)

        return context


class ProfileEditView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit-profile.html'
    success_url = '/users/profile/'

    def get_object(self):
        return self.request.user

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student-create.html'
    success_url = '/users/profile/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class StudentEditView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student-edit.html'
    success_url = "/users/profile"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs