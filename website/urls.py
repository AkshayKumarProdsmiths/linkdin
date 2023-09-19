from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
    #--------linkdin_profile---------
    path('user/<int:pk>/', views.linkdinprofile.as_view(), name='General-Information')

]