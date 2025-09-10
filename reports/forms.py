from django import forms
from django.core.exceptions import ValidationError
from .models import Document, Incident, ArchiveItem
import os

ALLOWED_EXTENSIONS = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png', '.mp4']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'file', 'pages', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'tags': forms.TextInput(attrs={'placeholder': 'Comma-separated tags'}),
        }

    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if uploaded_file:
            ext = os.path.splitext(uploaded_file.name)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                raise ValidationError(f'Unsupported file extension. Allowed: {", ".join(ALLOWED_EXTENSIONS)}')
        return uploaded_file

class IncidentForm(forms.ModelForm):
    class Meta:
        model = ArchiveItem
        fields = ['title', 'description', 'media_type', 'media', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a brief title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the incident', 'rows': 5}),
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'media': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
