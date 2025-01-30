from django.contrib import admin
from .models import *
from .models import Destination
from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.



from django.contrib import admin
from .models import Destination
from ckeditor.widgets import CKEditorWidget
from django import forms

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
        widgets = {
            'desc': CKEditorWidget(),
        }

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    form = DestinationForm

admin.site.register(Comments)
