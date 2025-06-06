import os
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import CustomUserCreationForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, FileResponse
from django.template import loader
from .forms import SongsForm, NewsForm, GalleryForm, LinkForm, DocumentForm, SetListForm, SetForm, AddDanceForm
from pages.models import Songs, News, Gallery, Links, Documents, CustomUser, SetList, Set
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django_renderpdf.views import PDFView
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet



def index (request):
  return render(request, 'index.html', {})
  #template = loader.get_template('index.html')
  #return HttpResponse(template.render())


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
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
    if request.user.is_authenticated:
        score = Songs.objects.filter(moderated='Yes').order_by('title').values()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(score, 5)
    
        try:
            items_page = paginator.page(page_num)
            items_page_items = items_page.object_list
        except PageNotAnInteger:
            items_page = paginator.page(1)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)
        #score = Songs.objects.all()
        return render(request, "music.html", { "items_page": items_page})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def musicMod(request):
    if request.user.is_authenticated:
        score = Songs.objects.all().order_by('title').values()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(score, 5)
    
        try:
            items_page = paginator.page(page_num)
            items_page_items = items_page.object_list
        except PageNotAnInteger:
            items_page = paginator.page(1)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)
        #score = Songs.objects.all()

        return render(request, "musicMod.html", { "items_page": items_page})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def search_music(request):
    if request.method == 'GET':
        value = request.GET['title']

        if value == '':
            messages.success(request, "Please enter a search criteria")
            items_page = Songs.objects.all()
        else:
            items_page = Songs.objects.filter(title__startswith = value)
            print('score2', items_page)
        return render(request, "music.html", {'items_page':items_page})


def add_tune(request):
    if request.user.is_authenticated:
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
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def delete_tune(request, id):
    if request.user.is_authenticated:
        song = get_object_or_404(Songs, id=id)
        song.delete()
        return redirect('music')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')


def download_music(request, name):
    if request.user.is_authenticated:
        file = os.path.join(settings.BASE_DIR, 'uploads/songs/',name)
        with open(file, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            #response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
        pdf.closed
    else:
        return render(request, 'login.html')



def edit_music(request, id):
    if request.user.is_authenticated:
        tune = Songs.objects.get(id=id)
        if request.method == 'POST':
            form = SongsForm(request.POST, instance=tune)
            if form.is_valid():
                form.save()
                return redirect('musicMod') # prepopulate the form with an existing band
        else:
            form = SongsForm(instance=tune)
                
        return render(request, 'edit_music.html',{'form': form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')


def update_file(request, id):
    if request.user.is_authenticated:
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
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')


def gallery(request):
    articles = Gallery.objects.all()
    ordering = ['article_created_at']
    return render(request, 'gallery.html', {'articles':articles})

def add_gallery_item(request):
    if request.user.is_authenticated:
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
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def delete_gallery_item(request, id):
    if request.user.is_authenticated:
        img = get_object_or_404(Gallery, id=id)
        img.delete()
        return redirect('gallery')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')



def add_news_item(request):
    if request.user.is_authenticated:
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
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')


def news(request):
    articles = News.objects.all()
    ordering = ['article_created_at']
    return render(request, 'news.html', {'articles':articles})

def delete_news_item(request, id):
    if request.user.is_authenticated:
        img = get_object_or_404(News, id=id)
        img.delete()
        return redirect('news')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')


def links(request):
    links = Links.objects.all()
    ordering = ['article_created_at']
    return render(request, 'links.html', {'links':links})

def delete_link(request, id):
    if request.user.is_authenticated:
        link = get_object_or_404(Links, id=id)
        link.delete()
        return redirect('links')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def add_link(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = LinkForm(request.POST)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('links')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = LinkForm()
        return render(request, 'add_link.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')


def edit_gallery(request, id):
    if request.user.is_authenticated:
        edit_img = Gallery.objects.get(id=id)
        if request.method == "POST":
            edit_img.heading= request.POST['heading']
            edit_img.content_text = request.POST['content_text']
            edit_img.save()        
            return redirect('gallery')
        print('here')
        edit_img = Gallery.objects.get(id=id)
        return render(request, 'edit_gallery.html', {"edit_img":edit_img})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def contact(request):

    return render(request, 'contact.html', {})

def documents(request):
    if request.user.is_authenticated:
        docs = Documents.objects.all().values()
        ordering = ['article_created_at']
        return render(request, 'documents.html', {'docs':docs})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def documentMod(request):
    if request.user.is_authenticated:
        docs = Documents.objects.all().values()
        ordering = ['article_created_at']
        return render(request, 'documentMod.html',{'docs':docs})
    else:
        return render(request, 'login.html')
        

def add_documents(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('documents')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = DocumentForm()
        return render(request, 'add_document.html', {'form':form})
    else:
        return render(request, 'login.html')

def download_documents(request, name):
    if request.user.is_authenticated:
        file = os.path.join(settings.BASE_DIR, 'upload/documents/',name)
        with open(file, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            #response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
        pdf.closedvalues_list
    else:
        return render(request, 'login.html')

def delete_document(request, id):
    if request.user.is_authenticated:
        docs = get_object_or_404(Documents, id=id)
        docs.delete()
        return redirect('documents')
    else:
        return render(request, 'login.html')
    
def create_set_list(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetListForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('music')
            else:
                print('')
        else:
            form = SetListForm()
        return render(request, 'create_set_list.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
def create_set(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('create_set_list')
            else:
                print('')
        else:
            form = SetForm()
        return render(request, 'create_set.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
def set(request):
    if request.user.is_authenticated:
        lists = Set.objects.values()
        ordering = ['order']
        return render(request, 'set.html', {'lists':lists})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')    

def view_set(request, id):
    if request.user.is_authenticated:
        items = SetList.objects.filter(set_id=id)
        title = Set.objects.get(id=id)
        return render(request, 'view_set.html', {'items':items, 'title':title})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
def add_dance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddDanceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('music')
            else:
                print('')
        else:
            form = AddDanceForm()
        return render(request, 'add_dance.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    

def generate_pdf(request, id): 
    response = HttpResponse(content_type='application/pdf') 
    response['Content-Disposition'] = 'filename="generate_pdf.pdf"' 
    doc = SimpleDocTemplate(response, pagesize=A4, title='Set List') 

    # Create a list to hold the table data 
    table_data = [['Tune', 'Dance', 'Notes', 'Set']]  # Add headers 
 
    # Fetch data from the database 
    for item in SetList.objects.filter(set_id=id): 
        table_data.append([item.song.title, item.dance.danceName, item.notes, item.set.setTitle])  # Add your fields 
 
    styles = getSampleStyleSheet()
    # Create a table 
    table = Table(table_data, colWidths=(2*inch, 2*inch, 2*inch, 2*inch)) 
    style = TableStyle([ 
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), 
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), 
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12), 
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige), 
        ('GRID', (0, 0), (-1, -1), 1, colors.black), 
    ]) 
    table.setStyle(style) 

    for item in SetList.objects.filter(set_id=id): 
        flowables = [
            Paragraph(item.set.setTitle, styles['Title']),
            Paragraph(item.set.venue, styles['Title']),
            Paragraph(item.set.setDate.strftime('%d-%m-%Y'), styles['Title']),
            table,
            Spacer(1 * inch, 1 * inch),
            Paragraph('Brampton Community Band', styles['Title']),
    ]
    def onFirstPage(canvas, doc):
        canvas.drawCentredString(100, 100, 'Text drawn with onFirstPage')

    

    # Build the PDF 
    doc.build(flowables, onFirstPage=onFirstPage) 
    
    return response

