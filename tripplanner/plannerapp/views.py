from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import tripRecm



# Create your views here.
def hm(request):
    return render(request, 'plannerapp/home.html')

def rg(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(response, "plannerapp/register.html", {"form": form})

def ls(request):
    return render(request, 'plannerapp/list.html')

def ed(request):
    return render(request, 'plannerapp/edit.html')

def dl(request):
    return render(request, 'plannerapp/daily.html')

def tripRecommendation(request):
	tripRecommendation = tripRecm.objects.all() #queryset containing all movies we just created
	return render(request=request, template_name="plannerapp/tripRecommendation.html", context={'tripRecommendation':tripRecommendation})