from django.urls import path
from .views import home, listaProj, newProj, editProj, preDelProj, delProj, listaModelDocs #, listaDocs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home-home'),
    path('Lista_Proj', listaProj, name='lista-proj'),
    path('New_Proj', newProj, name='new-proj'),
    path('Edit_Proj/<int:id>', editProj, name='edit-proj'),
    path('Pre_Del_Proj', preDelProj, name='pre-del-proj'),
    path('Del_Proj/<int:id>', delProj, name='del-proj'),

    path('Lista_Model_Docs', listaModelDocs, name='lista-model-docs'),
   # path('Lista_Docs', listaDocs, name='lista-docs'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
