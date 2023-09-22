from django.urls import path,include
from rest_framework import routers
from website.views import *

app_name = 'website'

router = routers.DefaultRouter()
router.register(r'GeneralInformation', GeneralInformationviewSet)

urlpatterns = [
     
      path('', include(router.urls),name=GeneralInformation),
    # path("", views.IndexView.as_view(), name="index"),
    # #--------linkdin_profile---------
    # path('user/<int:pk>/', views.linkdinprofile.as_view(), name='General-Information'),
    # path('add/', views.add_general_information, name='add_user'),
    # path("",views.index,name="index"),
    # path('api/create_user/', views.create_user, name='create_user_api'), 
]