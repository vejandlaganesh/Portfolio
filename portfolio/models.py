from django.db import models
class Portfolio(models.Model):
 name=models.CharField(max_length=120); headline=models.CharField(max_length=250); summary=models.TextField(); email=models.EmailField(); phone=models.CharField(max_length=40); linkedin=models.URLField(blank=True); github=models.URLField(blank=True); about=models.TextField(); resume=models.FileField(upload_to='resume/', blank=True, null=True); profile_photo=models.ImageField(upload_to='profile/', blank=True, null=True)
class Skill(models.Model):
 title=models.CharField(max_length=100); skills=models.TextField(); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Experience(models.Model):
 company=models.CharField(max_length=150); role=models.CharField(max_length=150); team=models.CharField(max_length=150,blank=True); start_date=models.DateField(blank=True,null=True); end_date=models.DateField(blank=True,null=True); is_current=models.BooleanField(default=False); location=models.CharField(max_length=100,blank=True); bullets=models.TextField(); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Project(models.Model):
 project_image=models.ImageField(upload_to='projects/', blank=True, null=True); title=models.CharField(max_length=180); category=models.CharField(max_length=100); description=models.TextField(); technologies=models.TextField(); github_url=models.URLField(blank=True); live_url=models.URLField(blank=True); featured=models.BooleanField(default=False); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Education(models.Model):
 institution=models.CharField(max_length=180); degree=models.CharField(max_length=180); duration=models.CharField(max_length=100); location=models.CharField(max_length=100,blank=True); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
class Certification(models.Model):
 name=models.CharField(max_length=180); organization=models.CharField(max_length=150); year=models.CharField(max_length=10); category=models.CharField(max_length=150,blank=True); cert_image=models.ImageField(upload_to='certs/', blank=True, null=True); cert_file=models.FileField(upload_to='certs/', blank=True, null=True); cert_url=models.URLField(blank=True); description=models.TextField(blank=True); order=models.IntegerField(default=0)
 class Meta: ordering=['order','id']
