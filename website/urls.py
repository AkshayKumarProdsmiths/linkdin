# from django.urls import path,include
# from rest_framework import routers
# from website.views import GeneralInformationviewSet, IndexView, linkdinprofile, add_general_information


# app_name = 'website'

# router = routers.DefaultRouter()
# router.register(r'GeneralInformation', GeneralInformationviewSet)

# urlpatterns = [
     
#       path('', include(router.urls),name=GeneralInformation),
#       path("", views.IndexView.as_view(), name="index"),
#     # #--------linkdin_profile---------
#      path('user/<int:pk>/', views.linkdinprofile.as_view(), name='General-Information'),
#      path('add/', views.add_general_information, name='add_user'),
#      path("",views.index,name="index"),
#     #path('api/create_user/', views.create_user, name='create_user_api'), 
# ]



from django.urls import path, include
from rest_framework import routers
from website.views import GeneralInformationviewSet, IndexView, linkdinprofile, add_general_information,EducationviewSet,AddressviewSet,LicensesCertificationsviewSet,PersonviewSet

app_name = 'website'

router = routers.DefaultRouter()
router.register(r'GeneralInformation', GeneralInformationviewSet)
router.register(r'Education', EducationviewSet)
router.register(r'Address', AddressviewSet)
router.register(r'Certification', LicensesCertificationsviewSet)
router.register(r'Person',PersonviewSet)


urlpatterns = [
    path('', include(router.urls), name='GeneralInformation'),
    path("", IndexView.as_view(), name="index"),  # Import IndexView correctly.
    
    # Import other views explicitly from your 'website.views' module.
    path('user/<int:pk>/', linkdinprofile.as_view(), name='General-Information'),
    path('add/', add_general_information, name='add_user'),
    path("", IndexView.as_view(), name="index"),  # Import IndexView again if needed.
    
    # Add other URL patterns related to your app here.
]
