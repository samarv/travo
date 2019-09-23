from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shoutout.models import organization, user, shoutout

from rest_framework.test import APIRequestFactory


class OrganizationTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('OrganizationList')
        response = self.client.post('/slack/org/',
                                    {
                                        "name": "org3",
                                        "slack_org_id": "wwddwdd",
                                        "channel_name": "wddwwddw",
                                        "channel_id": "dwwddww",
                                        "access_token": "wdwdwdw",
                                        "installation_date": "2019-09-23T11:49:49.858572Z",
                                        "bot_access_token": "wdwdwwddw"
                                    }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(organization.objects.count(), 1)
        self.assertEqual(organization.objects.get().name, 'org3')


class UserTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        self.client.post('/slack/org/',
                         {
                             "name": "org3",
                             "slack_org_id": "wwddwdd",
                             "channel_name": "wddwwddw",
                             "channel_id": "dwwddww",
                             "access_token": "wdwdwdw",
                             "installation_date": "2019-09-23T11:49:49.858572Z",
                             "bot_access_token": "wdwdwwddw"
                         }, format='json')
        url = '/slack/user/'
        data = {
            "org_id": 1,
            "slack_mem_id": "123432",
            "email": "samar@samar.com",
            "name": "samar",
            "avatar": "google.com"
        }
        response = self.client.post('/slack/user/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.objects.count(), 1)
        self.assertEqual(user.objects.get().name, 'samar')


class ShoutoutTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        self.client.post('/slack/org/',
                         {
                             "name": "org3",
                             "slack_org_id": "wwddwdd",
                             "channel_name": "wddwwddw",
                             "channel_id": "dwwddww",
                             "access_token": "wdwdwdw",
                             "installation_date": "2019-09-23T11:49:49.858572Z",
                             "bot_access_token": "wdwdwwddw"
                         }, format='json')
        url = '/slack/user/'
        data = {
            "org_id": 1,
            "slack_mem_id": "123432",
            "email": "samar@samar.com",
            "name": "samar",
            "avatar": "google.com"
        }
        response = self.client.post('/slack/user/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.objects.count(), 1)
        self.assertEqual(user.objects.get().name, 'samar')
        data = {
            "org_id": 1,
            "slack_mem_id": "123322432",
            "email": "bobr@samar.com",
            "name": "bob",
            "avatar": "google.com"
        }
        response = self.client.post('/slack/user/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.objects.count(), 2)
        data = {
            "giver_id": 1,
            "receiver_id": 2,
            "message": "good boi",
            "timestamps": "2019-09-23T10:10:51.768501Z",
            "message_ts": "134554323413"
        }
        response = self.client.post('/slack/shoutout/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(shoutout.objects.count(), 1)
        self.assertEqual(shoutout.objects.get().message, 'good boi')
