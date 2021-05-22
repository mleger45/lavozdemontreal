from django.http import HttpResponse

def auth(request):
    return HttpResponse("<h1>Auth callback received</h1>")