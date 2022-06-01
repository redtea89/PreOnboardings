from django.urls import path
from . import views


urlpatterns = [
    path('researches', views.ResearchCLView.as_view(), name='research-list'),
    path('researches/<int:pk>', views.ResearchRUDView.as_view(), name='research-detail'),
]