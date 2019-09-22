from django.http import HttpResponse
import json
import os
import slack
import asyncio
from rest_framework.parsers import FormParser

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])


def index(request):
    print("boo?")
    return HttpResponse("Hello, world!")


def send_async_message(channel='#bots', text='Hello world from async'):
    response = client.chat_postMessage(
        channel=channel,
        text=text

    )
    assert response["ok"]
    assert response["message"]["text"] == text


def send_dialog_open(dialog, trigger_id, channel='#bots', text='Hello world from async', ):
    response = client.dialog_open(
        dialog=dialog,
        trigger_id=trigger_id,
        channel=channel,
        text=text

    )
    assert response["ok"]
    assert response["message"]["text"] == text


def command(request):
    data = FormParser().parse(request)
    print(data)
    trigger_id = data['trigger_id']
    dialog = json.dumps({
        "title": 'Send some praise',
        "callback_id": 'submit-ticket',
        "submit_label": 'Submit',
        "elements": [
            {
                "label": 'Text',
                "type": 'text',
                "name": 'title',
                "value": "text",
                "hint": '30 second summary of the problem',
            },
            {
                "label": "Praise To",
                "name": "praise",
                "type": "select",
                "data_source": "users"
            }
        ],
    })
    send_dialog_open(trigger_id=trigger_id, dialog=dialog)
    return HttpResponse(status=200)
