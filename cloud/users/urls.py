from django.contrib import admin
from django.urls import path, include

from .views import (
    ProfileView,
    ProfileEditView,
    StudentCreateView,
    StudentEditView
)

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('student-create/', StudentCreateView.as_view(), name='student-create'),
    path('student-edit/<pk>/', StudentEditView.as_view(), name='student-edit'),
    path('edit-profile/', ProfileEditView.as_view(), name='edit-profile')
]
