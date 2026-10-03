from django.db import models
class Portfolio(models.Model):
 name=models.CharField(max_length=120); headline=models.CharField(max_length=250); summary=models.TextField(); email=models.EmailField(); phone=models.CharField(max_length=40); linkedin=models.URLField(blank=True); github=models.URLField(blank=True); about=models.TextField(); resume=models.FileField(upload_to='resume/', blank=True, null=True); profile_photo=models.ImageField(upload_to='profile/', blank=True, null=True); is_verified=models.BooleanField(default=True); verified_date=models.DateField(blank=True, null=True)
class Skill(models.Model):
 title=models.CharField(max_length=100); skills=models.TextField(); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Experience(models.Model):
 status=models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='published'); company=models.CharField(max_length=150); role=models.CharField(max_length=150); team=models.CharField(max_length=150,blank=True); start_date=models.DateField(blank=True,null=True); end_date=models.DateField(blank=True,null=True); is_current=models.BooleanField(default=False); location=models.CharField(max_length=100,blank=True); bullets=models.TextField(); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Project(models.Model):
 status=models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='published'); project_image=models.ImageField(upload_to='projects/', blank=True, null=True); title=models.CharField(max_length=180); category=models.CharField(max_length=100); description=models.TextField(); technologies=models.TextField(); github_url=models.URLField(blank=True); live_url=models.URLField(blank=True); project_category=models.CharField(max_length=20, choices=[('featured', 'Featured Project'), ('more', 'More Project')], default='more'); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Education(models.Model):
 institution=models.CharField(max_length=180); degree=models.CharField(max_length=180); duration=models.CharField(max_length=100); location=models.CharField(max_length=100,blank=True); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Certification(models.Model):
 name=models.CharField(max_length=180); organization=models.CharField(max_length=150); year=models.CharField(max_length=10); category=models.CharField(max_length=150,blank=True); cert_image=models.ImageField(upload_to='certs/', blank=True, null=True); cert_file=models.FileField(upload_to='certs/', blank=True, null=True); cert_url=models.URLField(blank=True); description=models.TextField(blank=True); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']


DOCUMENT_TYPES = (
    ('one_page', '1-Page Resume'),
    ('two_page', '2-Page Resume'),
    ('cover_letter', 'Cover Letter')
)

class ResumeDocument(models.Model):
    document_type = models.CharField(max_length=30, choices=DOCUMENT_TYPES, unique=True)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='resumes/')
    is_active = models.BooleanField(default=True)
    download_count = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_at']

class ResumeDownload(models.Model):
    resume = models.ForeignKey(ResumeDocument, on_delete=models.CASCADE, related_name='downloads')
    downloaded_at = models.DateTimeField(auto_now_add=True)

class CareerTimeline(models.Model):
    date_display = models.CharField(max_length=100)
    date_sort = models.DateField()
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    technologies = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='career_timeline/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_sort']

class Concept(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    description = models.TextField()
    projects = models.ManyToManyField(Project, blank=True, related_name="concepts")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

from django.core.validators import MinValueValidator, MaxValueValidator

class SystemStatus(models.Model):
    STATUS_CHOICES = [
        ("operational", "Operational"),
        ("degraded", "Degraded Performance"),
        ("partial_outage", "Partial Outage"),
        ("major_outage", "Major Outage"),
    ]
    component = models.CharField(max_length=150)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="operational")
    uptime_percentage = models.FloatField(default=99.9, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    last_checked = models.DateTimeField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["component"]

    def __str__(self):
        return self.component


class AdminActivityLog(models.Model):
    ACTION_CHOICES = [
        ("create", "Created"),
        ("update", "Updated"),
        ("delete", "Deleted"),
        ("publish", "Published"),
        ("unpublish", "Unpublished"),
    ]
    action = models.CharField(max_length=30, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100, blank=True)
    object_name = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PageVisit(models.Model):
    path = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    visitor_hash = models.CharField(max_length=64)