
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Employee, Project, DocumentModel, LdProj, Subject
from .forms import ProjectForm, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages
import numpy as np


def home(request):
    stauts_body = 'page-home'

    return render(request,'project_control/index.html', {'stauts_body': stauts_body})


#--------------------------------------------- Projects List
@login_required
def listaProj(request):
    stauts_body = ''

    GET = dict(request.POST)
    print(len(GET))

    Projects = Project.objects.all().order_by('-project_name')
    Employees = Employee.objects.all()

    docs_count = len(Projects)

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request,'project_control/lista-de-projetos.html', {'stauts_body':stauts_body, 'Projects':Projects, 'Employees':Employees, 'docs_count':docs_count,'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def newProj(request):

    Projects = Project.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/Lista_Proj')
    else:
        form = ProjectForm()
        return render(request, 'project_control/novo-projeto.html', {'form': form})


@login_required
def preDelProj(request):
    stauts_body = ''

    POST = dict(request.POST)
    print(POST)
    
    count_del_items = len(POST['_selected_action'])
    items = [int(i) for i in POST['_selected_action']]
    token = POST['csrfmiddlewaretoken']

    if len(items) > 1:
        return redirect('/admin/project_control/project/')

    else:
        Projects = Project.objects.all()
        ProjRead = []
        for a in items:
            print(a)
            for i in Projects:
                if i.id == a:
                    ProjRead.append([i.id, i.project_name])
            
        print(ProjRead)

        return render(request,'project_control/pre-deleta-projeto.html', {'stauts_body':stauts_body, 'ProjRead':ProjRead, 'count_del_items':count_del_items, 'items':items, 'token':token})


@login_required
def editProj(request, id):
    stauts_body = ''

    Projects = get_object_or_404(Project, pk=id)
    form = ProjectForm(instance=Projects)

    print(form)

    if(request.method == 'POST'):
        form = ProjectForm(request.POST, instance=Projects)

        if(form.is_valid()):
            #if Projects.policy == '0':
                #Projects.policy = '{}000000000000{}'.format(data_atual, length)
            Projects.save()
            return redirect('/Lista_Proj')
        else:
            return render(request,'project_control/editar-projetos.html', {'form':form, 'Projects':Projects})

    else:
        return render(request,'project_control/editar-projetos.html', {'form':form, 'Projects':Projects})


def delProj(request, id):
    Projects = get_object_or_404(Project, pk=id)
    Projects.delete()

    POST = dict(request.POST)
    print('---',POST)

    messages.info(request, 'Item deletado com sucesso!')

    return redirect('/Lista_Proj')


#--------------------------------------------- Documents Model
@login_required
def listaModelDocs(request):
    stauts_body = ''

    Projects = Project.objects.all().order_by('-project_name')
    Employees = Employee.objects.all()
    DocumentModels = DocumentModel.objects.all().order_by('-documment_name')

    docs_count = len(DocumentModels)

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request,'project_control/modelos-de-documentos.html', {'stauts_body':stauts_body, 'Projects':Projects, 'Employees':Employees, 'DocumentModels':DocumentModels, 'docs_count':docs_count, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def editDocMode(request, id):
    stauts_body = ''

    Projects = get_object_or_404(Project, pk=id)
    form = ProjectForm(instance=Projects)

    print(form)

    if(request.method == 'POST'):
        form = ProjectForm(request.POST, instance=Projects)

        if(form.is_valid()):
            #if Projects.policy == '0':
                #Projects.policy = '{}000000000000{}'.format(data_atual, length)
            Projects.save()
            return redirect('/Lista_Proj')
        else:
            return render(request,'project_control/editar-projetos.html', {'form':form, 'Projects':Projects})

    else:
        return render(request,'project_control/editar-projetos.html', {'form':form, 'Projects':Projects})


def delDocMode(request, id):
    Projects = get_object_or_404(Project, pk=id)
    Projects.delete()

    POST = dict(request.POST)
    print('---',POST)

    messages.info(request, 'Item deletado com sucesso!')

    return redirect('/Lista_Proj')


#--------------------------------------------- Lista de Documentos
@login_required
def listDocs(request, id):
    stauts_body = ''

    id_proj = id

    LdProjs = LdProj.objects.filter(proj_name_id=id_proj)
    Employees = Employee.objects.all()
    Subjects = Subject.objects.all().order_by('-subject_name')

    list_docs, list_id, list_proj, unique = [],[],[],[]
    for a in LdProjs:
        list_proj.append(a.proj_name)
        list_docs.append(a.subject_name)
        list_id.append(a.subject_name_id)

    unique_list_doc = list(set(list_docs))
    unique_list_id = list(set(list_id))

    #unique_list = len(np.unique(list_docs))
    for a in range(0, len(unique_list_doc)):
        unique.append([unique_list_id[a], unique_list_doc[a]])

    print('>>>>>>', unique_list_id, unique_list_doc)
 
    docs_count = len(unique)

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request,'project_control/lista-de-documentos.html', {'stauts_body':stauts_body, 'unique':unique,
                            'list_proj':list_proj, 'Employees':Employees, 'LdProjs':LdProjs, 'docs_count':docs_count, 'id_proj':id_proj, 'colaborador':colaborador, 
                            'photo_colab':photo_colab})


@login_required
def listDocsFilter(request, id):
    stauts_body = ''

    POST = dict(request.POST)

    id_sub = int(POST['action'][0])
    id_proj = int(POST['_id_proj'][0])

    LdProjs = LdProj.objects.filter(proj_name_id=id_proj).filter(subject_name_id=id_sub)
    Employees = Employee.objects.all()
    Subjects = Subject.objects.all().order_by('-subject_name')
 
    docs_count = len(LdProjs)

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request,'project_control/lista-de-documentos-filter.html', {'stauts_body':stauts_body, 'Subjects':Subjects, 'Employees':Employees, 'LdProjs':LdProjs, 'docs_count':docs_count, 'colaborador':colaborador, 'photo_colab':photo_colab})


'''

@login_required
def listaDocs(request):
    stauts_body = ''

    GET = dict(request.POST)
    print(len(GET))

    Projects = Project.objects.all().order_by('-project_name')
    Employees = Employee.objects.all()
    DocumentModels = DocumentModel.objects.all().order_by('-documment_name')

    token = 0
    proj = 0

    if len(GET) > 0:
        print('ok')
        token = 0
        proj = 0
        DocumentModels = DocumentModel.objects.all().order_by('-documment_name')

    else:
        token = 'x' #GET['csrfmiddlewaretoken']
        proj = 0 #GET['action']
        DocumentModels = DocumentModel.objects.filter(id=proj)

    docs_count = len(DocumentModels)

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request,'project_control/lista-de-documentos.html', {'stauts_body':stauts_body, 'Projects':Projects, 'Employees':Employees, 'DocumentModels':DocumentModels, 'proj':proj, 'docs_count':docs_count, 'token':token, 'colaborador':colaborador, 'photo_colab':photo_colab})


'''


'''


@login_required
def selectProjAction(request):

    POST = dict(request.POST)
    print(POST)
    
    count_del_items = len(POST['_selected_action'])
    items = [int(i) for i in POST['_selected_action']]
    token = POST['csrfmiddlewaretoken']

    if len(items) > 1:
        return redirect('/admin/project_control/project/')

    else:
        if POST['action'] == 'delete_selected':
            Projects = Project.objects.all()
            ProjRead = []
            for a in items:
                print(a)
                for i in Projects:
                    if i.id == a:
                        ProjRead.append([i.id, i.project_name])
                
            print(ProjRead)

            return render(request,'project_control/pre-deleta-projeto.html', {'stauts_body':stauts_body, 'ProjRead':ProjRead, 'count_del_items':count_del_items, 'items':items, 'token':token})
        
        elif POST['action'] == 'edite_selected':
            Projects = Project.objects.all()
            ProjRead = []
            for a in items:
                print(a)
                for i in Projects:
                    if i.id == a:
                        ProjRead.append([i.id, i.project_name])
                
            print(ProjRead)

            return redirect('/Edit_Proj/ProjRead.0.0')

'''

