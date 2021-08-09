from django.db import models
from django.contrib.auth import get_user_model

class Employee(models.Model): #Lista de Funcionários

    emp_name = models.CharField(max_length=255, verbose_name='NOME DO COLABORADOR')
    emp_office = models.CharField(max_length=255, verbose_name='FUNÇÃO')
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name

class Project(models.Model): #Títulos de projeto

    project_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Subject(models.Model): #Disciplinas do Projeto

    subject_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


class PageType(models.Model): #Tipo de folha

    name_page = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_page


class DocType(models.Model): #Tipo de Documento, MD, FD, etc

    name_doc = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_doc


class Pageformat(models.Model): #Formato de página

    name_format = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_format


class DocumentModel(models.Model): #Modelo de Documento

    documment_name = models.CharField(max_length=255, verbose_name='NOME DOCUMENTO')
    doc_code = models.ForeignKey(DocType, on_delete=models.CASCADE, verbose_name='CÓDIGO DOC')
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO DO DOCUMENTO')
    doc_type_page = models.ForeignKey(PageType, on_delete=models.CASCADE, verbose_name='PADRÃO DE FOLHA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.documment_name


class StatusDoc(models.Model): #Status do Projeto

    doc_status = models.CharField(max_length=50, verbose_name='STATUS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.doc_status


class Action(models.Model): #Lista de Acões

    action_type = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.action_type


class LdProj(models.Model): #Tabela = Lista de Documentos LD
    
    proj_name = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name_pattern = models.ForeignKey(DocumentModel, on_delete=models.CASCADE, verbose_name='NOME DO DOCUMENTO BASE')
    doc_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DO DOCUMENTO NO PROJETO')
    doc_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='NÚMERO DO DOCUMENTO')
    page_type = models.ForeignKey(PageType, on_delete=models.CASCADE, verbose_name='TIPO DE FOLHA')
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO')
    type_doc = models.ForeignKey(DocType, on_delete=models.CASCADE, verbose_name='TIPO DE DOCUMENTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.proj_name)


class ProjControl(models.Model): #Tabela = Lista de Documentos LD
    
    proj_name = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DO DOCUMENTO')
    doc_number = models.ForeignKey(DocType, on_delete=models.CASCADE, verbose_name='NÚMERO DO DOCUMENTO')
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='resp', verbose_name='RESPONSÁVEL')
    elab = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='elab', verbose_name='ELABORADOR')
    verif = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='verif', verbose_name='VERIFICADOR')
    aprov = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='aprov', verbose_name='APROVADOR')
    emiss = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='emiss', verbose_name='EMISSOR')
    status = models.ForeignKey(StatusDoc, on_delete=models.CASCADE, blank=True, null=True, verbose_name='STATUS')
    action = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True, verbose_name='AÇÃO')
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    comments = models.TextField()
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.proj_name)

        
class Upload(models.Model): #Upload de arquivos
    arq = models.FileField(upload_to='uploads/', help_text='localizar Arquivo')
    update_arq = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.arq)





""" class Cotation(models.Model): #Tabela de Cotação de projeto
    
    proj_name = models.ForeignKey(MyProject, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name_pattern = models.ForeignKey(DocumentStandard, on_delete=models.CASCADE, verbose_name='DOCUMENTO BASE')
    doc_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DOCUMENTO')
    cod_doc_type = models.ForeignKey(DocT, on_delete=models.CASCADE, verbose_name='CÓDIGO DOC')
    page_type = models.ForeignKey(PageT, on_delete=models.CASCADE, verbose_name='TIPO PÁGINA')
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO')
    qt_page = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True, verbose_name='QT PÁGINA')
    qt_hh = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True, verbose_name='QT HH')
    cost_doc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='CUSTO DOCUMENTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.subject_name)

        
class ProjectValue(models.Model): #Upload de arquivos
    cost_by_hh = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='CUSTO HH')
    cost_by_doc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,verbose_name='CUSTO FOLHA')
    cost_by_A1 = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,verbose_name='CUSTO A1 EQ')

    def __str__(self):
        return str(self.cost_by_hh)
 """