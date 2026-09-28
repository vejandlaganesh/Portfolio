import os
from datetime import date
from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *

def seed():
 # NOTE: the admin user is no longer created here. seed() runs on every public page
 # view, and it used to create a superuser with a guessable fallback password.
 # Create it with `python manage.py createsuperuser` (build.sh does this on deploy
 # from the DJANGO_SUPERUSER_* environment variables).
 if not Portfolio.objects.exists(): Portfolio.objects.create(name='Vejandla Ganesh Sharma',headline='Building intelligent digital experiences.',summary='B.Tech graduate in AI/ML with hands-on experience building Generative AI applications and Full Stack web solutions.',email='ganeshvejandla@gmail.com',phone='+91 9490360499',linkedin='https://linkedin.com/in/vejandla-ganesh',github='https://github.com/vejandlaganesh',about='Focused on Generative AI, full-stack development, and QA automation.')
 if not Skill.objects.exists():
  for i,(a,b) in enumerate([('AI / ML & GenAI','Machine Learning, Deep Learning, Generative AI, LLMs, NLP, Computer Vision, OpenCV, Scikit-learn'),('Programming','Python, Java, JavaScript, TypeScript, SQL'),('Full Stack','HTML5, CSS3, React, Node.js, Express.js, Django'),('QA & Automation','Playwright, Karate, API Testing, POM'),('Databases','MySQL, Firebase Firestore'),('Tools','Git, GitHub, VS Code, Maven')]): Skill.objects.create(title=a,skills=b,order=i)
 if not Experience.objects.exists(): Experience.objects.create(company='PUBLICIS SAPIENT',role='QA Automation Intern',team='Sustain Engineering Team',start_date=date(2026,5,1),end_date=date(2026,6,1),is_current=False,location='Hyderabad, India',bullets='Reduced manual regression effort by 60%+ using Playwright and Karate.\nDeveloped 30+ reusable Playwright scripts using POM and JavaScript.\nAutomated REST API workflows with Karate, validating JSON and database state.')
 if not Project.objects.exists():
  ps=[('Edu Carrier','AI • CAREER GUIDANCE','AI-powered career guidance platform for careers, streams, courses, exams, resources and personalized pathways.','React.js, TypeScript, Vite, Tailwind CSS, Node.js, Express.js, Firebase Firestore, Gemini GenAI','','https://career-guidance-f6x9.onrender.com/',1),('Scriptoria AI','GENERATIVE AI • FILM','AI-powered film pre-production platform for story, storyboard and shot planning.','Python, Django, Generative AI, Groq GenAI, Image Generation','https://github.com/vejandlaganesh/Scriptoria','',0),('NewEdu','AI • EDUCATION','Full-stack AI-powered learning platform for personalized practical education with student, teacher, parent and admin modules.','Generative AI, Groq API, HTML, CSS, JavaScript, MySQL','','',0),('Playwright Automation Framework','QA • AUTOMATION','Reusable Playwright framework using JavaScript, POM, ExcelJS and data-driven testing.','JavaScript, Playwright, ExcelJS, POM','','',0)]
  for i,p in enumerate(ps): Project.objects.create(title=p[0],category=p[1],description=p[2],technologies=p[3],github_url=p[4],live_url=p[5],featured=p[6],order=i)
 if not Education.objects.exists():
  for i,p in enumerate([('KITS Akshar Institute of Technology','B.Tech in Artificial Intelligence and Machine Learning','10/2022 — 04/2026','Yanamadala, India'),('NARAYANA Junior College','IPE','08/2020 — 08/2022',''),('Bhashyam IIT Foundation','SSC','05/2015 — 07/2020','')]): Education.objects.create(institution=p[0],degree=p[1],duration=p[2],location=p[3],order=i)
 if not Certification.objects.exists():
  for i,p in enumerate([('Software Engineer Intern','HackerRank','2026'),('SDLC – Software Development Life Cycle','Udemy','2026'),('Advanced Prompting in GPT-4','Adobe Learning Manager','2026'),('SQL (Intermediate)','HackerRank','2026'),('Python Programming','Aajhub','2025'),('Full Stack Web Development','Aajhub','2025')]): Certification.objects.create(name=p[0],organization=p[1],year=p[2],order=i)

def guard(request, code):
 if code != settings.PORTFOLIO_ADMIN_CODE: return HttpResponseForbidden('Invalid admin code')
 if not request.user.is_authenticated: return redirect('admin_login', code=code)
 return None

def admin_login(request, code):
 if code != settings.PORTFOLIO_ADMIN_CODE: return HttpResponseForbidden('Invalid admin code')
 seed()
 if request.user.is_authenticated: return redirect('admin_dashboard', code=code)
 error = None
 if request.method == 'POST':
  user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
  if user:
   auth_login(request, user)
   return redirect('admin_dashboard', code=code)
  else:
   error = 'Invalid username or password.'
 return render(request, 'admin/login.html', {'code': code, 'error': error})

def admin_logout(request, code):
 auth_logout(request)
 return redirect('admin_login', code=code)

def home(request):
 seed(); return render(request,'home.html',{'profile':Portfolio.objects.first(),'skills':Skill.objects.all(),'experiences':Experience.objects.all(),'projects':Project.objects.all(),'total_projects_count':Project.objects.count(),'education':Education.objects.all(),'certifications':Certification.objects.all()})

def admin_dashboard(request,code):
 e=guard(request, code)
 if e:return e
 seed(); return render(request,'admin/dashboard.html',{'code':code,'profile':Portfolio.objects.first(),'counts':[Project.objects.count(),Skill.objects.count(),Experience.objects.count(),Education.objects.count(),Certification.objects.count()]})

def _month_to_date(val):
 # <input type="month"> submits 'YYYY-MM'; store it as the 1st of that month.
 try: return date.fromisoformat(val + '-01') if val else None
 except ValueError: return None

CLEARABLE_FILE_FIELDS = ('project_image','resume','profile_photo','cert_image','cert_file')

def _apply_post(obj, fields, request):
 # Copy submitted values onto obj IN MEMORY ONLY. The caller decides whether to save,
 # so a failed validation can re-render the form with the user's input intact.
 names = [x[0] for x in fields]
 for name in names:
  if name in request.FILES: setattr(obj,name,request.FILES[name])
  elif name in ('start_date','end_date'): setattr(obj,name,_month_to_date(request.POST.get(name)))
  elif name in request.POST: setattr(obj,name,request.POST.get(name,''))
  if name in CLEARABLE_FILE_FIELDS and name not in request.FILES and request.POST.get('clear_'+name)=='on': setattr(obj,name,None)
 if 'featured' in names: obj.featured = request.POST.get('featured')=='on'
 if 'is_current' in names:
  obj.is_current = request.POST.get('is_current')=='on'
  if obj.is_current: obj.end_date = None

def form(request,code,title,fields,obj=None,back='admin_dashboard'):
 e=guard(request, code)
 if e:return e
 error = None
 if request.method=='POST':
  if obj is None: obj=fields[0][1]()
  _apply_post(obj,fields,request)
  if 'start_date' in [x[0] for x in fields]:
   if not obj.start_date: error = 'Start Date is required.'
   elif not obj.is_current and not obj.end_date: error = 'End Date is required unless currently working here.'
   elif obj.end_date and obj.end_date < obj.start_date: error = 'End Date cannot be before Start Date.'
  if not error:
   obj.save(); return redirect(back,code=code)
 return render(request,'admin/form.html',{'code':code,'title':title,'fields':fields,'object':obj,'back':back,'error':error})

def profile_edit(request,code):
 p=Portfolio.objects.first() or Portfolio.objects.create()
 return form(request,code,'Edit Profile',[(x,Portfolio) for x in ['name','headline','summary','email','phone','linkedin','github','about','profile_photo']],p,'admin_dashboard')

def resume_edit(request,code):
 p=Portfolio.objects.first() or Portfolio.objects.create()
 return form(request,code,'Manage Resume',[(x,Portfolio) for x in ['resume']],p,'admin_dashboard')

def collection(request,code,title,model,add,edit,delete):
 e=guard(request, code)
 if e:return e
 return render(request,'admin/list.html',{'code':code,'title':title,'items':model.objects.all(),'add':add,'edit':edit,'delete':delete})

def add_obj(request,code,title,model,fields,back): return form(request,code,title,[(f,model) for f in fields],None,back)
def edit_obj(request,code,pk,title,model,fields,back): return form(request,code,title,[(f,model) for f in fields],get_object_or_404(model,pk=pk),back)
def del_obj(request,code,pk,model,back):
 e=guard(request, code)
 if e:return e
 if request.method=='POST':get_object_or_404(model,pk=pk).delete()
 return redirect(back,code=code)

def projects(request,code):return collection(request,code,'Projects',Project,'project_add','project_edit','project_delete')
def project_add(request,code):return add_obj(request,code,'Add New Project',Project,['project_image','title','category','description','technologies','github_url','live_url','featured'],'projects')
def project_edit(request,code,pk):return edit_obj(request,code,pk,'Edit Project',Project,['project_image','title','category','description','technologies','github_url','live_url','featured'],'projects')
def project_delete(request,code,pk):return del_obj(request,code,pk,Project,'projects')
def skills(request,code):return collection(request,code,'Skills',Skill,'skill_add','skill_edit','skill_delete')
def skill_add(request,code):return add_obj(request,code,'Add New Skill',Skill,['title','skills'],'skills')
def skill_edit(request,code,pk):return edit_obj(request,code,pk,'Edit Skill',Skill,['title','skills'],'skills')
def skill_delete(request,code,pk):return del_obj(request,code,pk,Skill,'skills')
def experiences(request,code):return collection(request,code,'Experience',Experience,'experience_add','experience_edit','experience_delete')
def experience_add(request,code):return add_obj(request,code,'Add Experience',Experience,['company','role','team','start_date','end_date','is_current','location','bullets'],'experiences')
def experience_edit(request,code,pk):return edit_obj(request,code,pk,'Edit Experience',Experience,['company','role','team','start_date','end_date','is_current','location','bullets'],'experiences')
def experience_delete(request,code,pk):return del_obj(request,code,pk,Experience,'experiences')
def education(request,code):return collection(request,code,'Education',Education,'education_add','education_edit','education_delete')
def education_add(request,code):return add_obj(request,code,'Add Education',Education,['institution','degree','duration','location'],'education')
def education_edit(request,code,pk):return edit_obj(request,code,pk,'Edit Education',Education,['institution','degree','duration','location'],'education')
def education_delete(request,code,pk):return del_obj(request,code,pk,Education,'education')
def certifications(request,code):return collection(request,code,'Certifications',Certification,'certification_add','certification_edit','certification_delete')
def certification_add(request,code):return add_obj(request,code,'Add Certification',Certification,['name','organization','year','category','cert_image','cert_file','cert_url','description'],'certifications')
def certification_edit(request,code,pk):return edit_obj(request,code,pk,'Edit Certification',Certification,['name','organization','year','category','cert_image','cert_file','cert_url','description'],'certifications')
def certification_delete(request,code,pk):return del_obj(request,code,pk,Certification,'certifications')
