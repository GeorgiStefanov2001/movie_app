from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the movies app index")
