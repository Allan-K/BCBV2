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
    path('musicMod', views.musicMod, name='musicMod'),    
    path('music', views.music, name='music'),
    path('songs/<str:name>', views.download_music, name='download_music'), 
    path('documents/<str:name>', views.download_documents, name='download_document'),   
    path('edit_music/<int:id>/change/', views.edit_music, name='edit_music'),
    path('delete_tune/<int:id>', views.delete_tune, name='delete_tune'),
    path('add_tune/', views.add_tune, name='add_tune'),
    path('search_music/', views.search_music, name='search_music'),
    path('gallery/', views.gallery, name='gallery'),
    path('edit_gallery/<int:id>', views.edit_gallery, name='edit_gallery'),
    path('links/', views.links, name='links'),
    path('add_link/', views.add_link, name='add_link'),
    path('delete_gallery_item/<int:id>', views.delete_gallery_item, name='delete_gallery_item'),
    path('delete_news_item/<int:id>', views.delete_news_item, name='delete_news_item'),
    path('delete_link/<int:id>', views.delete_link, name='delete_link'),
    path('delete_document/<int:id>', views.delete_document, name='delete_document'),
    path('news/', views.news, name='news'),
    path('add_news_item/', views.add_news_item, name='add_news_item'),
    path('gallery/', views.gallery, name='gallery'),
    path('add_gallery_item/', views.add_gallery_item, name='add_gallery_item'),
    path('links/', views.links, name='links'),
    path('documents/', views.documents, name='documents'),
    path('documentMod/', views.documentMod, name='documentMod'),
    path('add_documents/', views.add_documents, name='add_documents'),
    path('contact/', views.contact, name='contact'),
    path('create_set_list/', views.create_set_list, name='create_set_list'),
    path('create_set/', views.create_set, name='create_set'),
    path('set/', views.set, name='set'),
    path('view_set/<int:id>', views.view_set, name='view_set'),

]

#development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)