from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from website.models import GeneralInformation
from website.serializers import GeneralInformationSerializer

class GeneralInformationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('website:generalinformation-list') 


    def test_get_general_information_list(self):
        GeneralInformation.objects.create(name="User1", student_at="School1", connections="10",
                                          profile_language="English", public_profile_url="https://example.com/user1")
        # GeneralInformation.objects.create(name="User2", student_at="School2", connections="20",
        #                                   profile_language="Spanish", public_profile_url="https://example.com/user2")

    def test_create_general_information(self):
        data = {
            "name": "User3",
            "student_at": "School3",
            "connections": "30",
            "profile_language": "French",
            "public_profile_url": "https://example.com/user3",
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
        self.assertEqual(GeneralInformation.objects.count(), 1)

       
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['student_at'], data['student_at'])
        self.assertEqual(response.data['connections'], data['connections'])
        self.assertEqual(response.data['profile_language'], data['profile_language'])
        self.assertEqual(response.data['public_profile_url'], data['public_profile_url'])

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = GeneralInformationSerializer(GeneralInformation.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data,)