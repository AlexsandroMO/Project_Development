from django.urls import path
from .views import home, listaDocs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home-home'),
    path('Lista_Docs', listaDocs, name='lista-docs'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
