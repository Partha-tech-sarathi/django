from django.urls import path

from .views import HospitalView, HospitalDetailView


urlpatterns = [

    path('hospital/', HospitalView.as_view()),

    path('hospital/<int:id>/', HospitalDetailView.as_view()),

]