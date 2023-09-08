from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('news/',api_views.EssayListCreateAPIView.as_view(), name='essay-list'),
    path('news/<int:pk>/',api_views.EssayDetailAPIView.as_view(), name='essay-detail')
]


# FUNCTION BASED VIEWS
# urlpatterns = [
#     path('news/',api_views.essay_list_create_api_view, name='essay-list'),
#     path('news/<int:pk>/',api_views.essay_detail_api_view, name='essay-detail')
# ]