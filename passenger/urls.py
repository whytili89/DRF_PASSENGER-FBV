from django.urls import path
from passenger import views

urlpatterns = [
    path('passengers/',views.passenger_list),
    path('passenger/<int:pk>', views.passenger_detail),
]