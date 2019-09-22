from django.http import HttpResponse
import os
import slack
import asyncio

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


def command(request):
    print("boo")
    send_async_message()
    return HttpResponse(status=200)
