import os
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import CustomUserCreationForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, FileResponse
from django.template import loader
from .forms import SongsForm, NewsForm, GalleryForm
from pages.models import Songs, News, Gallery
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import UpdateView

def index (request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():edit_music
        form.save()
            #login(request, user)

        return redirect("/")
    else:
        form= CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def loginBCB(request):
    if request.method == "POST":
        # Attempt to sign user inpk.id
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
        else:edit_music
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

def delete_tune(request, id):
    song = get_object_or_404(Songs, id=id)
    song.delete()
    return redirect('music')
    pass



def download_music(request, name):
    file = os.path.join(settings.BASE_DIR, 'uploads/songs/',name)
    with open(file, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        #response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed


def edit_music(request, id):
    edit_score = Songs.objects.get(id=id)
    if request.method == "POST":
        edit_score.title = request.POST['title']
        edit_score.desc = request.POST['description']
        edit_score.set = request.POST['is_set']
        edit_score.save()        
        return redirect('music')
    print('here')
    edit_score = Songs.objects.get(id=id)
    context = {"edit_score":edit_score}
    return render(request, 'edit_music.html', context=context)

def update_file(request, id):
    if request.method == 'POST':
        file = request.FILES['update_file']

        file_name = request.FILES['update_file'].name
        folder = 'songs/'
        fs = FileSystemStorage()
        file = fs.save(file.name, file)
        print(file)
        fileurl = fs.url(file)
        report = file_name

        Songs.objects.filter(id=id).update(file=file)

        return redirect('music')
    else:
        return render(request, 'update_file.html')


def gallery(request):
    articles = Gallery.objects.all()
    ordering = ['article_created_at']
    return render(request, 'gallery.html', {'articles':articles})

def add_gallery_item(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        print('here')
        if form.is_valid():
            form.save()
            return redirect('gallery')
        else:
            print('Not Here')
    else:
        print('here 2')
        form = GalleryForm()
    return render(request, 'add_gallery_item.html', {'form':form})


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
    ordering = ['article_created_at']
    return render(request, 'news.html', {'articles':articles})


def links(request):

    return render(request, 'links.html', {})

def contact(request):

    return render(request, 'contact.html', {})