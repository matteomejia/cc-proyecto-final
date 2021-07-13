from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cloud.users.models import Student

from .models import Workshop

# Create your views here.

class WorkshopListView(ListView):
    queryset = Workshop.objects.filter(status=1)
    template_name = 'workshops/workshop-list.html'


class WorkshopDetailView(DetailView):
    queryset = Workshop.objects.all()
    template_name = 'workshops/workshop-detail.html'
    context_object_name = 'workshop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['students'] = Student.objects.filter(parent=self.request.user)

        return context