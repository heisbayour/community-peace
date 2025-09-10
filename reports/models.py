from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pages = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=255, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class ArchiveItem(models.Model):
    MEDIA_CHOICES = [
        ('Image', 'Image'),
        ('Document', 'Document'),
        ('Video', 'Video'),
    ]
    STATUS_CHOICES = [
        ('Resolved', 'Resolved'),
        ('Ongoing', 'Ongoing'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='reports/')
    media_type = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    thumbnail = models.ImageField(upload_to='reports/thumbnails/', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

# models.py
class Incident(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Resolved', 'Resolved'),
    ]
    MEDIA_CHOICES = [
        ('Image', 'Image'),
        ('Document', 'Document'),
        ('Video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='incidents/')
    media_type = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ongoing')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
