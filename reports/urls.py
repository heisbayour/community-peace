from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='all_documents'),
    path('archive/', views.archive_list, name='full_archive'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('about/', views.about, name='about'),
    path('report/', views.report_incident, name='report_incident'),
]
