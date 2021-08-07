from django.urls import path
from .views import home, listaProj, newProj, editProj, preDelProj, delProj, \
listaModelDocs, editDocMode, delDocMode, \
listDocs, listDocsFilter  #, listaDocs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home-home'),
    #----Projects
    path('Lista_Proj', listaProj, name='lista-proj'),
    path('New_Proj', newProj, name='new-proj'),
    path('Pre_Del_Proj', preDelProj, name='pre-del-proj'),
    path('Edit_Proj/<int:id>', editProj, name='edit-proj'),
    path('Del_Proj/<int:id>', delProj, name='del-proj'),
    #----Document Model
    path('Lista_Model_Docs', listaModelDocs, name='lista-model-docs'),
    path('Edit_Doc_Mode/<int:id>', editDocMode, name='edit-doc-mode'),
    path('Del_Doc_Mode/<int:id>', delDocMode, name='del-doc-mode'),
    #----List Docs
    path('List_Docs/<int:id>', listDocs, name='list-docs'),
    path('List_Docs_Filter/<int:id>', listDocsFilter, name='list-docs-filter'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
