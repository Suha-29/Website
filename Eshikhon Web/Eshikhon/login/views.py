from django.shortcuts import render
from django.http import HttpResponse

from .models import User_info
from django.shortcuts import redirect
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-timestamp')[:10]
    return render(request,"login/index.html",{'posts': posts})

def post_status(request):
    if request.method == 'POST':
        username = request.POST.get('author')
        status_content = request.POST.get('status')

        # Creat and save the new post
        Post.objects.create(author=username, content=status_content)

        # Redirect to the home view after posting
        return redirect('home')
    
    # If it's a GET requset, just redirect to home
    return redirect('home')

def login(request):
    return HttpResponse("Welcome to Eshikhon login page.")

def signup(request):
    users = User_info.objects.all()
    output = ""
    for user in users:
        output += user.fname +"<==>"+ user.lname +"<==>"+ user.email +"<==>"+ user.username + "\n"
    return HttpResponse("Welcome to Eshikhon sign-up page."+output)

def shop(request):
    return render(request,"login/shop.html",{})