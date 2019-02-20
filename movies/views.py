from django.http import HttpResponse

#this is the index view for the movies app
def index(request):
    return HttpResponse("This is the movies app index")
