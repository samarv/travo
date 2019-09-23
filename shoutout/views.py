from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import FormParser
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
    print("index", response)
    return HttpResponse("Hello, world!")


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
                "name": "name",
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
    print("interactive", data)
    return HttpResponse(status=200)
