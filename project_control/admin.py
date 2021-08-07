from django.contrib import admin
from . models import Project, Subject, DocumentModel, Action, StatusDoc, Employee, Upload, PageType, DocType, Pageformat, LdProj, ProjControl


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name','emp_office','photo','user')

class ProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','code','comments')
    list_display = ('id','project_name','company','code','comments','created_at','update_at')
    

class SubjectAdmin(admin.ModelAdmin):
    fields = ('subject_name',)
    list_display = ('id','subject_name', 'created_at','update_at')


class PageTypeAdmin(admin.ModelAdmin):
    fields = ('name_page',)
    list_display = ('name_page','created_at','update_at')


class DocTypeAdmin(admin.ModelAdmin):
    fields = ('name_doc',)
    list_display = ('name_doc','created_at','update_at')


class PageformatAdmin(admin.ModelAdmin):
    fields = ('name_format',)
    list_display = ('name_format','created_at','update_at')
    

class DocumentModeldAdmin(admin.ModelAdmin):
    fields = ('documment_name', 'doc_code','format_doc','doc_type_page')
    list_display = ('documment_name', 'doc_code','format_doc','doc_type_page','created_at','update_at')


class StatusDocAdmin(admin.ModelAdmin):
    fields = ('doc_status',)
    list_display = ('doc_status', 'created_at','update_at')
    

class ActionAdmin(admin.ModelAdmin):
    fields = ('action_type',)
    list_display = ('action_type', 'created_at','update_at')


class LdProjAdmin(admin.ModelAdmin):
    fields = ('proj_name', 'subject_name', 'doc_name_pattern','doc_name', 'doc_number','page_type','format_doc')
    list_display = ('id','proj_name', 'subject_name', 'doc_name_pattern','doc_name','doc_number','page_type','format_doc','created_at','update_at') 


class ProjControlAdmin(admin.ModelAdmin):
    fields = ('proj_name', 'subject_name','doc_name','doc_number','responsible','elab','verif','aprov','emiss','status','action','date_start','date_end')
    list_display = ('proj_name', 'subject_name','doc_name','doc_number','responsible','elab','verif','aprov','emiss','status','action','date_start','date_end','created_at','update_at') 


class UploadAdmin(admin.ModelAdmin):
    fields = ('arq',)
    list_display = ('arq', 'update_arq')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(PageType, PageTypeAdmin)
admin.site.register(DocType, DocTypeAdmin)
admin.site.register(Pageformat, PageformatAdmin)
admin.site.register(DocumentModel, DocumentModeldAdmin)
admin.site.register(Action)
admin.site.register(StatusDoc)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(LdProj, LdProjAdmin)
admin.site.register(ProjControl, ProjControlAdmin)
admin.site.register(Upload)
