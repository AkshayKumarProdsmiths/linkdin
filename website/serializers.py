from rest_framework import serializers
from .models import *

class GeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = '__all__'
class EducationSerializer(serializers.ModelSerializer):
    #forkey = GeneralInformationSerializer()
    class Meta:
        model = Education
        fields = '__all__'
class AddressSerializer(serializers.ModelSerializer):
    #forkey = GeneralInformationSerializer()
    class Meta:
        model = Address
        fields = '__all__'
class LicensesCertificationsSerializer(serializers.ModelSerializer):
    #forkey = GeneralInformationSerializer()
    class Meta:
        model = LicensesCertifications
        fields = '__all__'
class PersonSerializer(serializers.ModelSerializer):
    #forkey = GeneralInformationSerializer()
    class Meta:
        model = Person
        fields = '__all__'