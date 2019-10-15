from django.shortcuts import render, redirect
from .forms import MovieModelForm
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context={
        'movies':movies,
    }
    return render(request,'index.html',context) 