from django.urls import path
from countryapp import views

app_name='country'

urlpatterns = [

    path('', views.index,name='country_index'),
]