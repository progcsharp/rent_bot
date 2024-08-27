from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="base_index"),
    path("<str:f>", views.index, name="index"),
    path('news/', views.info, name="info"),
    path('settings/', views.setting, name="settings")
]
