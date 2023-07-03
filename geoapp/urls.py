from django.urls import path

from .views import GeometryView

app_name = 'geoapp'

urlpatterns = [
    path('projection/', GeometryView.as_view(), name='geometry'),
]
