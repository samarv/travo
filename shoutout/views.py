from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.parsers import FormParser, JSONParser

from .models import organization, user, shoutout
from .serializers import OrganizationSerializer, UserSerializer, ShoutoutSerializer
from rest_framework import generics

import json
import os
import slack
import asyncio


client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])


def index(request):
    getPrams = request.GET
    code = getPrams["code"]
    # verify the code and get access tokens!
    response = client.oauth_access(client_id="711954789234.757475024355",
                                   client_secret="530630e9e46ad76fee5b3ef0e9baf43d", code=code)
    data = {
        "name": response["team_name"],
        "slack_org_id": response["team_id"],
        "channel_name": response["incoming_webhook"]["channel"],
        "channel_id": response["incoming_webhook"]["channel_id"],
        "access_token": response["access_token"],
        "bot_access_token": response["bot"]["bot_access_token"],
    }
    serializer = OrganizationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)


def login(request):
    client_id = os.environ['SLACK_CLIENT_ID']
    print("login", request.body)
    # TO-DO Why isn't client-id passing to landing page
    return render(request, 'landing.html', {'client_id': client_id})


def send_async_message(channel='#bots', text='Hello world from async'):
    response = client.chat_postMessage(
        channel=channel,
        text=text

    )
    assert response["ok"]
    assert response["message"]["text"] == text


def send_dialog_open(trigger_id, channel_id='CMQ777QG6'):
    dialog = json.dumps({
        "title": 'Send some praise',
        "callback_id": 'submit-ticket',
        "submit_label": 'Submit',
        "elements": [
            {
                "label": "Shoutout to",
                "name": "user",
                "type": "select",
                "data_source": "users"
            },
            {
                "label": 'for',
                "type": 'textarea',
                "name": 'shoutout',
                "value": ""
            }
        ],
    })
    response = client.dialog_open(
        dialog=dialog,
        trigger_id=trigger_id,
        channel_id=channel_id,
    )


def command(request):
    data = FormParser().parse(request)
    print(data)
    trigger_id = data['trigger_id']
    text = data['text']
    send_dialog_open(trigger_id=trigger_id, channel_id="CMQ777QG6")
    return HttpResponse(status=200)


def interactive(request):
    data = FormParser().parse(request)
    # payload = data.get("payload")
    data = data.dict()
    pl = json.loads(data["payload"])
    print(pl)
    sender_id = pl["user"]["id"]
    receiver_id = pl["submission"]["user"]
    shoutout_text = pl["submission"]["shoutout"]
    text = sender_id + " gave a shout out to " + receiver_id + " - " + shoutout_text
    send_async_message(text=text)
    return HttpResponse(status=200)


class OrganizationList(generics.ListCreateAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer


class UserList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class ShoutoutList(generics.ListCreateAPIView):
    queryset = shoutout.objects.all()
    serializer_class = ShoutoutSerializer


class ShoutoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = shoutout.objects.all()
    serializer_class = ShoutoutSerializer
