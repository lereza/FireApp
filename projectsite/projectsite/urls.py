from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('stations', views.map_station, name='map-station'),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),

]
