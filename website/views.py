from django.http import JsonResponse,HttpResponse
from django.views import generic
from .models import *
from .forms import GeneralInformationForm
from django.shortcuts import render,redirect
from .forms import GeneralInformationForm
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from website.serializers import *


class GeneralInformationviewSet(viewsets.ModelViewSet):
         queryset = GeneralInformation.objects.all()
         serializer_class= GeneralInformationSerializer

class EducationviewSet(viewsets.ModelViewSet):
         queryset = Education.objects.all()
         serializer_class= EducationSerializer

class AddressviewSet(viewsets.ModelViewSet):
         queryset = Address.objects.all()
         serializer_class= AddressSerializer

class LicensesCertificationsviewSet(viewsets.ModelViewSet):
         queryset = LicensesCertifications.objects.all()
         serializer_class= LicensesCertificationsSerializer

class PersonviewSet(viewsets.ModelViewSet):
         queryset = Person.objects.all()
         serializer_class= PersonSerializer






class IndexView(generic.ListView):
    template_name = "website/index.html"
    context_object_name = "latest_GeneralInformation_list"

    def get_queryset(self):
    
        return GeneralInformation.objects.all()

class linkdinprofile(generic.DetailView):
     model = GeneralInformation
     template_name = 'website/linkdinprofile.html'  
     context_object_name = 'user' 

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()  

        context['resources'] = Resources.objects.filter(user=user)
        context['education'] = Education.objects.filter(user=user)
        context['address'] = Address.objects.filter(user=user)
        context['skills'] = Skills.objects.filter(user=user)
        context['certifrcate'] = LicensesCertifications.objects.filter(user=user)
        context['people_also_viewed'] = Person.objects.filter(user=user)

        return context
     
def add_general_information(request):
      if request.method == 'POST':
        form = GeneralInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:index')  # Redirect to the admin index page or any other desired URL
      else:
        form = GeneralInformationForm()
      return render(request, 'website/forms.html', {'form': form})

