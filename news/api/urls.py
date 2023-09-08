from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('news/',api_views.essay_list_create_api_view, name='essay-list'),
]