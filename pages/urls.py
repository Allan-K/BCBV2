from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('loginBCB', views.loginBCB, name='loginBCB'),
    path('logoutBCB', views.logoutBCB, name='logoutBCB'),
    path('update_password/', views.update_password, name='update_password'),
    path('music/', views.music, name='music'),
    path('music/songs/<str:name>', views.download_music, name='download_music'),   
    path('edit_music/<int:id>/', views.edit_music, name='edit_music'),
    path('add_tune/', views.add_tune, name='add_tune'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('add_news_item/', views.add_news_item, name='add_news_item'),
    path('gallery/', views.gallery, name='gallery'),
    path('add_gallery_item/', views.add_gallery_item, name='add_gallery_item'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),
    #path('process_add_tune/', views.process_add_tune, name='process_add_tune'),
    #path('songs/', views.success, name='download_tune'),

]

#development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)