from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def command(request):
    print(request)
    return HttpResponse("Hello, world!")
