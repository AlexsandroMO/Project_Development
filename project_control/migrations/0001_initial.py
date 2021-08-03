# Generated by Django 3.2.6 on 2021-08-03 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(max_length=12)),
                ('created_st', models.DateTimeField(auto_now_add=True)),
                ('update_st', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_doc', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documment_name', models.CharField(max_length=255, verbose_name='NOME DOCUMENTO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('doc_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.doctype', verbose_name='CÓDIGO DOC')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=255, verbose_name='NOME DO COLABORADOR')),
                ('emp_office', models.CharField(max_length=255, verbose_name='FUNÇÃO')),
                ('photo', models.FileField(blank=True, null=True, upload_to='uploads/photos/', verbose_name='FOTO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USUÁRIO')),
            ],
        ),
        migrations.CreateModel(
            name='Pageformat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_format', models.CharField(max_length=15)),
                ('created_aty', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_page', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('comments', models.TextField()),
                ('code', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_status', models.CharField(max_length=50)),
                ('created_st', models.DateTimeField(auto_now_add=True)),
                ('update_st', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arq', models.FileField(help_text='localizar Arquivo', upload_to='uploads/')),
                ('update_arq', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='NOME DO DOCUMENTO')),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('comments', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_control.action', verbose_name='AÇÃO')),
                ('aprov', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aprov', to='project_control.employee', verbose_name='APROVADOR')),
                ('doc_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.doctype', verbose_name='NÚMERO DO DOCUMENTO')),
                ('elab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elab', to='project_control.employee', verbose_name='ELABORADOR')),
                ('emiss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emiss', to='project_control.employee', verbose_name='EMISSOR')),
                ('proj_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.project', verbose_name='PROJETO')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp', to='project_control.employee', verbose_name='RESPONSÁVEL')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_control.statusdoc', verbose_name='STATUS')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.subject', verbose_name='DISCIPLINA')),
                ('verif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verif', to='project_control.employee', verbose_name='VERIFICADOR')),
            ],
        ),
        migrations.CreateModel(
            name='LdProj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='NOME DO DOCUMENTO NO PROJETO')),
                ('doc_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='NÚMERO DO DOCUMENTO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('doc_name_pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.documentmodel', verbose_name='NOME DO DOCUMENTO BASE')),
                ('format_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.pageformat', verbose_name='FORMATO')),
                ('page_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.pagetype', verbose_name='TIPO DE FOLHA')),
                ('proj_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.project', verbose_name='PROJETO')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.subject', verbose_name='DISCIPLINA')),
            ],
        ),
        migrations.AddField(
            model_name='documentmodel',
            name='doc_type_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.pagetype', verbose_name='TIPO PÁGINA'),
        ),
        migrations.AddField(
            model_name='documentmodel',
            name='format_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_control.pageformat', verbose_name='FORMATO DO DOCUMENTO'),
        ),
    ]