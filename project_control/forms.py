from django import forms
from .models import Project, LdProj


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'company','code','comments')


class LdProjForm(forms.ModelForm):
    class Meta:
        model = LdProj
        fields = ('proj_name','subject_name','doc_name_pattern','doc_name','doc_number','page_type','format_doc')


    