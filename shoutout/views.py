from django.http import HttpResponse
import os
import slack as sl
import asyncio

client = sl.WebClient(
    token='xoxp-711954789234-717019077457-770822092487-4717d514e7ab0a08f1f140ff302aa9f2')


def index(request):
    print("boo?")
    return HttpResponse("Hello, world!")


def send_async_message(channel='#bots', text='Hello world from async'):
    response = client.chat_postMessage(
        channel=channel,
        text=text
    )
    assert response["ok"]
    assert response["message"]["text"] == "Hello world from async"


def command(request):
    send_async_message()
    return HttpResponse(status=200)
