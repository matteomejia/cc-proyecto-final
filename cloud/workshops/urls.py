from django.contrib import admin
from django.urls import path, include

from .views import (
    WorkshopListView,
    WorkshopDetailView
)

app_name = 'workshops'

urlpatterns = [
    path('', WorkshopListView.as_view(), name='workshop-list'),
    path('<slug:slug>/', WorkshopDetailView.as_view(), name='workshop-detail')
]
