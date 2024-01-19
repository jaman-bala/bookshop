from django.urls import path
from backend.apps.search import views

app_name = 'search'

urlpatterns = [
    path('', views.search, name="search")
]
