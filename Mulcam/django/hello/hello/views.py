from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def test(request):
    return HttpResponse("<h1><a href='/hello01'>return</a></h1>")

def my(request):
    return HttpResponse("<h1>전동준</h1>")