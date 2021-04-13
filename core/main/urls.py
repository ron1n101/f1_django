from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('teams/', views.TeamViews.as_view(), name='teams'),
    path('gallery/', views.GalleryViews.as_view(), name='gallery'),
    path('feedback/', views.feedback, name='feedback'),
    path('teams/<str:slug>/', views.teams_details, name='teams_detail_url'),
]