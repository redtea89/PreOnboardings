from django.urls import path
from . import views


urlpatterns = [
    path('groups', views.GroupCLView.as_view(), name='group-list'),
    path('groups/<int:pk>', views.GroupRUDView.as_view(), name='group-detail'),
    path('restaurants', views.RestaurantCLView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>', views.RestaurantRUDView.as_view(), name='restaurant-detail'),
    path('kpi/restaurant', views.KpiPerRestaurantView.as_view(), name='kpi-restaurant'),
    path('kpi/payment', views.KpiPerPaymentView.as_view(), name='kpi-payment'),
    path('kpi/partysize', views.KpiPerPartysizeView.as_view(), name='kpi-partysize'),
]