from rest_framework import serializers
from .models import *

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
class LicensesCertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensesCertifications
        fields = '__all__'
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class GeneralInformationSerializer(serializers.ModelSerializer):
    education_set = EducationSerializer(many=True)
    address_set = AddressSerializer(many=True)
    licenses_certifications = LicensesCertificationsSerializer(many=True, read_only=True)
    person_set = PersonSerializer(many=True)
    class Meta:
        model = GeneralInformation
        fields =  ['name','student_at','connections','profile_language','public_profile_url','education_set','address_set','licenses_certifications','person_set'] 