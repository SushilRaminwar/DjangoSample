from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
# Create your views here.
def homepage(request):
    #return HttpResponse("asdasd")
    return render(request=request,
                  template_name="catalog/home.html",
                  context={"tutorials":Tutorial.objects.all})

def homepage1(request):
    return HttpResponse("asdqwe")