from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post,Follow
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")

    following_users = set(
        Follow.objects.filter(follower=request.user)
        .values_list('following_id', flat=True)
    )

    return render(request, 'home.html', {
        'posts': posts,
        'following_users': following_users
    })
    #return HttpResponse('hello world')
    
def post_detail(request,slug): # to view single post
    post=get_object_or_404(Post,slug=slug)
    return render(request,'post_detail.html',{'post':post})

@login_required
def post_create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        cover_image=request.FILES.get('cover_image')
        Post.objects.create(title=title,content=content,cover_image=cover_image,user=request.user)
        return redirect('home')
    return render(request,'post_create.html')

@login_required
def post_edit(request,slug):
    post=get_object_or_404(Post,slug=slug,user=request.user)
    if request.method=='POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        if request.FILES.get('cover_image'):
            post.cover_image=request.FILES.get('cover_image')

        post.slug=''
        post.save()
        return redirect('home')
    return render(request,'post_edit.html',{'post':post})


@login_required
def post_delete(request,slug):
    post=get_object_or_404(Post,slug=slug,user=request.user)
    if request.method=="POST":
        post.delete()
        return redirect('home')

@login_required
def friends_feed(request):
    following_users=Follow.objects.filter(follower=request.user).values_list('following',flat=True)
    posts=Post.objects.filter(user__in=following_users).order_by('-created_at')
    return render(request,'friends_feed.html',{'posts':posts})

    
@login_required
def follow_user(request,username):
    user_to_follow=get_object_or_404(User,username=username)
    if user_to_follow!=request.user:
        Follow.objects.get_or_create(follower=request.user,following=user_to_follow)
    return redirect('friends_feed')


@login_required
def unfollow_user(request,username):
    user_to_unfollow=get_object_or_404(User,username=username)
    Follow.objects.filter(follower=request.user,following=user_to_unfollow).delete()
    return redirect('friends_feed')