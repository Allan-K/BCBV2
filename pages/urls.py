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
    path('music', views.music, name='music'),
    path('music/songs/<str:name>', views.download_music, name='download_music'),   
    path('edit_music/<int:id>', views.edit_music, name='edit_music'),
    path('delete_tune/<int:id>', views.delete_tune, name='delete_tune'),
    path('add_tune/', views.add_tune, name='add_tune'),
    path('search_music/', views.search_music, name='search_music'),
    path('gallery/', views.gallery, name='gallery'),
    path('delete_gallery_item/<int:id>', views.delete_gallery_item, name='delete_gallery_item'),
    path('news/', views.news, name='news'),
    path('add_news_item/', views.add_news_item, name='add_news_item'),
    path('gallery/', views.gallery, name='gallery'),
    path('add_gallery_item/', views.add_gallery_item, name='add_gallery_item'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),

]

#development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)