from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Document, ArchiveItem
from .forms import DocumentForm, IncidentForm
from datetime import date as dt
import PyPDF2
import docx


# Home page
def home(request):
    documents = Document.objects.filter(approved=True)
    archive_items = ArchiveItem.objects.all()
    form = DocumentForm()
    context = {
        'documents': documents,
        'archive_items': archive_items,
        'form': form,
    }
    return render(request, 'reports/index.html', context)

# Get involved page
def get_involved(request):
    return render(request, 'reports/get_involved.html')

# Document upload
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            uploaded_file = request.FILES['file']
            ext = uploaded_file.name.split('.')[-1].lower()

            # Calculate pages
            try:
                if ext == 'pdf':
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    doc.pages = len(pdf_reader.pages)
                elif ext == 'docx':
                    document = docx.Document(uploaded_file)
                    paragraphs = len(document.paragraphs)
                    doc.pages = max(1, paragraphs // 30)  # simple heuristic
                else:
                    doc.pages = 0
            except Exception:
                doc.pages = 0

            doc.approved = False
            doc.save()
            messages.success(request, 'Document uploaded successfully and awaiting approval.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error uploading your document.')
    else:
        form = DocumentForm()

    documents = Document.objects.filter(approved=True)
    archive_items = ArchiveItem.objects.all()
    context = {
        'form': form,
        'documents': documents,
        'archive_items': archive_items,
    }
    return render(request, 'reports/index.html', context)

# Document list page
def document_list(request):
    documents = Document.objects.filter(approved=True)
    context = {'documents': documents}
    return render(request, 'reports/reports.html', context)

# About page
def about(request):
    return render(request, 'reports/about.html')

# Archive page
def archive_list(request):
    archive_items = ArchiveItem.objects.all()
    context = {'archive_items': archive_items}
    return render(request, 'reports/archive.html', context)


# New: Incident report page
def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            # Automatically set date if not in form
            incident.date = dt.today()
            incident.save()
            messages.success(request, "Incident reported successfully!")
            return redirect('reports:all_documents')
        else:
            messages.error(request, "There was an error submitting the incident.")
    else:
        form = IncidentForm()
    return render(request, 'reports/reports.html', {'form': form})