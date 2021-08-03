
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Employee, Project, DocumentModel
#from .forms import ProjectForm, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages

def home(request):
    stauts_body = 'page-home'
    return render(request,'project_control/index.html', {'stauts_body': stauts_body})


@login_required
def listaDocs(request):
    stauts_body = ''

    Projects = Project.objects.all().order_by('-project_name')
    Employees = Employee.objects.all()
    DocumentModels = DocumentModel.objects.all().order_by('-documment_name')

    #proj = 0

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request,'project_control/lista-de-documentos.html', {'stauts_body':stauts_body, 'Projects':Projects, 'Employees':Employees, 'DocumentModels':DocumentModels, 'colaborador':colaborador, 'photo_colab':photo_colab})