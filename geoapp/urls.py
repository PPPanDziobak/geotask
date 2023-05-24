from django.urls import path

from . import views
from .views import GeometryView

app_name = 'geoapp'

urlpatterns = [
    # path('', views.home, name='homeee'),
    path('projection/', GeometryView.as_view(), name='geometry'),

]
