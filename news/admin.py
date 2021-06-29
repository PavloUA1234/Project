from django.contrib import admin
from django import forms
from .models import Articles
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticlesAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Articles
        fields = '__all__'

class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm


admin.site.register(Articles, ArticlesAdmin)