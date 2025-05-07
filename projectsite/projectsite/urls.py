from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, city_data, ChartView,PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, FireStationListView, FireStationCreateView, FireStationUpdateView, FireStationDeleteView, IncidentListView, IncidentCreateView, IncidentUpdateView, IncidentDeleteView, LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView, FireTruckListView, FireTruckCreateView, FireTruckUpdateView, FireTruckDeleteView, firefighter_list, firefighter_create, firefighter_update, firefighter_delete

from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multipleBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('fire-incidents-map/', views.fire_incidents_map, name='fire-incidents-map'),
    path('fire-stations/', FireStationListView.as_view(), name='fire_station_list'),
    path('city_data/', views.city_data, name='city_data'),
    path('fire-stations/new/', FireStationCreateView.as_view(), name='fire_station_create'),
    path('fire-stations/<int:pk>/edit/', FireStationUpdateView.as_view(), name='fire_station_update'),
    path('fire-stations/<int:pk>/delete/', FireStationDeleteView.as_view(), name='fire_station_delete'),
    path('incidents/', IncidentListView.as_view(), name='incident_list'),
    path('incidents/add/', IncidentCreateView.as_view(), name='incident_create'),
    path('incidents/<int:pk>/edit/', IncidentUpdateView.as_view(), name='incident_update'),
    path('incidents/<int:pk>/delete/', IncidentDeleteView.as_view(), name='incident_delete'),
    path('locations/', LocationListView.as_view(), name='location_list'),
    path('locations/add/', LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/edit/', LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', LocationDeleteView.as_view(), name='location_delete'),
    path('firetrucks/', FireTruckListView.as_view(), name='firetruck_list'),
    path('firetrucks/create/', FireTruckCreateView.as_view(), name='firetruck_create'),
    path('firetrucks/<int:pk>/update/', FireTruckUpdateView.as_view(), name='firetruck_update'),
    path('firetrucks/<int:pk>/delete/', FireTruckDeleteView.as_view(), name='firetruck_delete'),
     path('firefighters/', views.firefighter_list, name='firefighter_list'),
    path('firefighters/new/', views.firefighter_create, name='firefighter_create'),
    path('firefighters/<int:pk>/edit/', views.firefighter_update, name='firefighter_update'),
    path('firefighters/<int:pk>/delete/', views.firefighter_delete, name='firefighter_delete'),
    path('weatherconditions/', views.weatherconditions_list, name='weatherconditions_list'),
    path('weatherconditions/<int:pk>/', views.weatherconditions_detail, name='weatherconditions_detail'),
    path('weatherconditions/create/', views.weatherconditions_create, name='weatherconditions_create'),
    path('weatherconditions/<int:pk>/update/', views.weatherconditions_update, name='weatherconditions_update'),
    path('weatherconditions/<int:pk>/delete/', views.weatherconditions_delete, name='weatherconditions_delete'),
]