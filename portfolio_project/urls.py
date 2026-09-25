from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
 path('',views.home,name='home'),
 path('portfolio-admin/<str:code>/',views.admin_login,name='admin_login'),
 path('portfolio-admin/<str:code>/dashboard/',views.admin_dashboard,name='admin_dashboard'),
 path('portfolio-admin/<str:code>/logout/',views.admin_logout,name='admin_logout'),
 path('portfolio-admin/<str:code>/profile/',views.profile_edit,name='profile_edit'),
 path('portfolio-admin/<str:code>/resume/',views.resume_edit,name='resume_edit'),
 path('portfolio-admin/<str:code>/projects/',views.projects,name='projects'),path('portfolio-admin/<str:code>/projects/add/',views.project_add,name='project_add'),path('portfolio-admin/<str:code>/projects/<int:pk>/edit/',views.project_edit,name='project_edit'),path('portfolio-admin/<str:code>/projects/<int:pk>/delete/',views.project_delete,name='project_delete'),
 path('portfolio-admin/<str:code>/skills/',views.skills,name='skills'),path('portfolio-admin/<str:code>/skills/add/',views.skill_add,name='skill_add'),path('portfolio-admin/<str:code>/skills/<int:pk>/edit/',views.skill_edit,name='skill_edit'),path('portfolio-admin/<str:code>/skills/<int:pk>/delete/',views.skill_delete,name='skill_delete'),
 path('portfolio-admin/<str:code>/experience/',views.experiences,name='experiences'),path('portfolio-admin/<str:code>/experience/add/',views.experience_add,name='experience_add'),path('portfolio-admin/<str:code>/experience/<int:pk>/edit/',views.experience_edit,name='experience_edit'),path('portfolio-admin/<str:code>/experience/<int:pk>/delete/',views.experience_delete,name='experience_delete'),
 path('portfolio-admin/<str:code>/education/',views.education,name='education'),path('portfolio-admin/<str:code>/education/add/',views.education_add,name='education_add'),path('portfolio-admin/<str:code>/education/<int:pk>/edit/',views.education_edit,name='education_edit'),path('portfolio-admin/<str:code>/education/<int:pk>/delete/',views.education_delete,name='education_delete'),
 path('portfolio-admin/<str:code>/certifications/',views.certifications,name='certifications'),path('portfolio-admin/<str:code>/certifications/add/',views.certification_add,name='certification_add'),path('portfolio-admin/<str:code>/certifications/<int:pk>/edit/',views.certification_edit,name='certification_edit'),path('portfolio-admin/<str:code>/certifications/<int:pk>/delete/',views.certification_delete,name='certification_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
