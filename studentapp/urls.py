from django.urls import path
from studentapp import views

app_name='student'

urlpatterns = [

    path('', views.index,name='student_index'),
]