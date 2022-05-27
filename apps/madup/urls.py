from django.urls import path

from .views import AdvertiserCLView, AdvertiserRUDView, AnalysisView

urlpatterns = [
    path('advertisers', AdvertiserCLView.as_view(), name='advertiser-list'),
    path('advertisers/<int:pk>', AdvertiserRUDView.as_view(), name='advertiser-detail'),
    path('analysis', AnalysisView.as_view(), name='analysis-view')
]