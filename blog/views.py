from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Post
# Create your views here.
def signup(request) :
    if request.method=='POST' :
        name=request.POST['uname']
        username=request.POST['uemail']
        password=request.POST['upassword']
        user=User.objects.create_user(name,username,password)
        user.save()
        return redirect('/loginn')
    return render(request,'blog/signup.html')

def loginn(request) :
     if request.method=='POST' :
         username=request.POST['email']
         password=request.POST['upassword']
         user = authenticate(username=username, password=password)
         if user is not None :
             login(request,user)
             messages.success(request,'Login successfull')
             return redirect('/')
         else :
             messages.error(request,'Invalid Credentials')
             return redirect('/signup')
     return render(request,'blog/login.html')
    
        
def signout(request) :
    logout(request)
    messages.success(request,'User logged out')
    return redirect('/loginn')

def home(request) :
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
    

def newpost(request) :
    if request.method=='POST' :
        title=request.POST['title']
        content=request.POST['content']
        post=Post(title=title,content=content,user=request.user)
        post.save()
        return redirect('/')
    return render(request,'blog/newpost.html')

def mypost(request) :
    user = request.user  # Get the currently logged-in user
    posts = Post.objects.filter(user=user).order_by('-date')
    return render(request,'blog/mypost.html',{'posts':posts})