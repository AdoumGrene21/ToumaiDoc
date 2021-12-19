from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from ancienSujet.models import Document

class DocumentsForm(ModelForm):
    model = Document
    fields = ['nom', 'description','document', 'type', 'niveau']