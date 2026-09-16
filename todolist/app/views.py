from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

# Create your views here.
def task_home(request):
    tasks=Task.objects.all().order_by('-completed_on')
    return render(request,'home.html',{'tasks':tasks})


@login_required
def add_task(request):
    if request.method=='POST':
        title= request.POST.get('title')
        description =request.POST.get('description')
        image=request.FILES.get('image')
        completed=request.POST.get('completed')
        Task.objects.create(title=title,description=description,image=image,completed=completed,user=request.user)
        return redirect('task_home')
    return render(request,'add_task.html')


@login_required
def delete_task(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    task.delete()
    return redirect('task_home')


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed 
    task.save()
    return redirect('task_home')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        re_password=request.POST.get('re_password')
        if password!=re_password:
            messages.error(request,'password dosnt match')
            return redirect('sign_pop')
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return redirect('sign_pop')
        if '@' not in email and '.' not in email.split('@')[-1]:
            messages.error(request,'invalid email')
            return redirect('sign_pop')
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            return redirect('sign_pop')
        user=User.objects.create_user(username=username,email=email,password=password)
        user = authenticate(
    request,
    username=username,
    password=password
)

        if user is not None:
            login(request,user)
            return redirect('task_home')
    return render(request,'signup.html')

def login_user(request):
    if request.method=='POST':
        password=request.POST.get('password')
        if request.POST.get('identifier'):
            username=request.POST.get('identifier')
            user=authenticate(request,username=username,password=password)
            
        elif request.POST.get('email'):
            wemail=request.POST.get('email')
            user_obj = User.objects.filter(email=wemail).first()
            if user_obj:
                user=authenticate(request,username=user_obj.username,password=password)
                
            else:
                user=None
        if user is not None:
                login(request,user)
                return redirect('task_home')

        
        messages.error(request,'invalid credentials')
        return redirect('login')
    return render(request,'login.html')

def logout_user(request):
        logout(request)
        return redirect('task_home')

            



            



        
