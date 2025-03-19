from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import CustomUserCreationForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse, FileResponse
from django.template import loader
from .forms import SongsForm, NewsForm
from pages.models import Songs, News
from django.core.files.storage import FileSystemStorage

def index (request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, user)

            return redirect("/")
    else:
        form= CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def loginBCB(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse("index"))
            return render(request, "index.html")
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logoutBCB(request):
    logout(request)
    return render(request, "index.html")

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        print(current_user)
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password has been updated.  Please log in again")
                #login(request, current_user)
                return redirect('index')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                print("failure")
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "User must be logged in to do this")
        return redirect('loginBCB')
    
def music(request):
    score = Songs.objects.all()
    return render(request, "music.html", {'score': score})


def add_tune(request):
    if request.method == 'POST':
        form = SongsForm(request.POST, request.FILES)
        print('here')
        if form.is_valid():
            form.save()
            return redirect('music')
        else:
            print('Not Here')
    else:
        print('here 2')
        form = SongsForm()
    return render(request, 'add_tune.html', {'form':form})


def gallery(request):

    return render(request, 'gallery.html', {})

def add_news_item(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        print('here')
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            print('Not Here')
    else:
        print('here 2')
        form = NewsForm()
    return render(request, 'add_news_item.html', {'form':form})


def news(request):
    articles = News.objects.all()
    return render(request, 'news.html', {'articles':articles})


def links(request):

    return render(request, 'links.html', {})

def contact(request):

    return render(request, 'contact.html', {})