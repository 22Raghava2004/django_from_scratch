from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.http import JsonResponse
from .models import Movies,Watchlist
import json

# Create your views here.
#--------public view this is the hom page where it is therer

def home(request):
    movies=Movies.objects.all()
    genres=Movies.objects.values_list('genre',flat=True).distinct()
    return render(request,'home.html',
                  {'movies':movies,
                   'genres':genres
                   })

def movie_details(request,pk):
    movie=get_object_or_404(Movies,pk=pk)
    in_watchlist=False
    if request.user.is_authenticated:
        in_watchlist=Watchlist.objects.filter(user=request.user,movie=movie).exists()
        return render(request,'movie_details.html',{'movie':movie,'in_watchlist':in_watchlist
                    })
def search_movies(request):
    query=request.GET.get('q', '')
    movies=Movies.objects.filter(title__icontains=query) if query else []

    data =[{
        'id': m.id,
        'title':m.title,
        'genre':m.genre,
        'poster':m.poster.url if m.poster else '',
    
    } for m in movies]
    return JsonResponse({'movies':data})

#------- Watchlist Views (JS fetch calls this )----

@login_required
def watchlist_add(request):
    if request.method=='POST':
        data= json.loads(request.body)
        movie_id=data.get('movie_id')
        movie=get_object_or_404(Movies,pk=movie_id)
        watchlist, created=Watchlist.objects.get_or_create(
            user=request.user,
            movie=movie
        )
        return JsonResponse({
            
            'success':True,
            'message':'movie added' if created else 'already exists',
            
        
        })
    return JsonResponse({'success':False})

@login_required
def watchlist_remove(request):
    if request.method=='POST':
        data=json.loads(request.body)
        movie_id=data.get('movie_id')
        Watchlist.objects.filter(user=request.user,movie_id=movie_id
                                 ).delete()
        return JsonResponse({'success':True,'message':'removed the selected from watchlist'})
    return JsonResponse({'success':False})

@login_required
def watchlist_view(request):
    watchlist=Watchlist.objects.filter(user=request.user).order_by('-added_on')
    return render(request,'watchlist.html',{'watchlist':watchlist})

def upload_movie(request):
    pass

def login_view(request):
    pass
def signup_view(request):
    pass
def logout_view(request):
    pass