from django.urls import path, re_path
from django.views.static import serve
from portfolio import views
from django.conf import settings
urlpatterns=[
 path('robots.txt', views.robots_txt, name='robots_txt'),
 path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
 path('',views.home,name='home'),
 path('portfolio-admin/<str:code>/',views.admin_login,name='admin_login'),
 path('portfolio-admin/<str:code>/dashboard/',views.admin_dashboard,name='admin_dashboard'),
 path('portfolio-admin/<str:code>/logout/',views.admin_logout,name='admin_logout'),

    path('status/', views.status_page, name='status_page'),
    path('portfolio-admin/<str:code>/status/', views.status_list, name='status_list'),
    path('portfolio-admin/<str:code>/status/<int:pk>/edit/', views.status_edit, name='status_edit'),


    path('learn/', views.learn_public, name='learn'),
    path('portfolio-admin/<str:code>/concepts/', views.concept_list, name='concept_list'),
    path('portfolio-admin/<str:code>/concepts/add/', views.concept_add, name='concept_add'),
    path('portfolio-admin/<str:code>/concepts/<int:pk>/edit/', views.concept_edit, name='concept_edit'),
    path('portfolio-admin/<str:code>/concepts/<int:pk>/delete/', views.concept_delete, name='concept_delete'),


    path('portfolio-admin/<str:code>/timeline/', views.timeline_list, name='timeline_list'),
    path('portfolio-admin/<str:code>/timeline/add/', views.timeline_add, name='timeline_add'),
    path('portfolio-admin/<str:code>/timeline/<int:pk>/edit/', views.timeline_edit, name='timeline_edit'),
    path('portfolio-admin/<str:code>/timeline/<int:pk>/delete/', views.timeline_delete, name='timeline_delete'),


    path('resume/', views.resume_public_center, name='resume_public_center'),
    path('resume/<int:pk>/download/', views.resume_download, name='resume_download'),
    path('portfolio-admin/<str:code>/resume-center/', views.admin_resume_center, name='admin_resume_center'),
    path('portfolio-admin/<str:code>/resume-center/add/', views.admin_resume_add, name='admin_resume_add'),
    path('portfolio-admin/<str:code>/resume-center/<int:pk>/edit/', views.admin_resume_edit, name='admin_resume_edit'),
    path('portfolio-admin/<str:code>/resume-center/<int:pk>/delete/', views.admin_resume_delete, name='admin_resume_delete'),


    path('projects/compare/', views.project_compare, name='project_compare'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),

 path('portfolio-admin/<str:code>/profile/',views.profile_edit,name='profile_edit'),
 path('portfolio-admin/<str:code>/resume/',views.resume_edit,name='resume_edit'),
 path('portfolio-admin/<str:code>/preview/project/<int:pk>/', views.preview_project, name='preview_project'),
 path('portfolio-admin/<str:code>/projects/',views.projects,name='projects'),path('portfolio-admin/<str:code>/projects/add/',views.project_add,name='project_add'),path('portfolio-admin/<str:code>/projects/<int:pk>/edit/',views.project_edit,name='project_edit'),path('portfolio-admin/<str:code>/projects/<int:pk>/delete/',views.project_delete,name='project_delete'),
 path('portfolio-admin/<str:code>/skills/',views.skills,name='skills'),path('portfolio-admin/<str:code>/skills/add/',views.skill_add,name='skill_add'),path('portfolio-admin/<str:code>/skills/<int:pk>/edit/',views.skill_edit,name='skill_edit'),path('portfolio-admin/<str:code>/skills/<int:pk>/delete/',views.skill_delete,name='skill_delete'),
 path('portfolio-admin/<str:code>/experience/',views.experiences,name='experiences'),path('portfolio-admin/<str:code>/experience/add/',views.experience_add,name='experience_add'),path('portfolio-admin/<str:code>/experience/<int:pk>/edit/',views.experience_edit,name='experience_edit'),path('portfolio-admin/<str:code>/experience/<int:pk>/delete/',views.experience_delete,name='experience_delete'),
 path('portfolio-admin/<str:code>/education/',views.education,name='education'),path('portfolio-admin/<str:code>/education/add/',views.education_add,name='education_add'),path('portfolio-admin/<str:code>/education/<int:pk>/edit/',views.education_edit,name='education_edit'),path('portfolio-admin/<str:code>/education/<int:pk>/delete/',views.education_delete,name='education_delete'),
 path('portfolio-admin/<str:code>/certifications/',views.certifications,name='certifications'),path('portfolio-admin/<str:code>/certifications/add/',views.certification_add,name='certification_add'),path('portfolio-admin/<str:code>/certifications/<int:pk>/edit/',views.certification_edit,name='certification_edit'),path('portfolio-admin/<str:code>/certifications/<int:pk>/delete/',views.certification_delete,name='certification_delete'),
 path('ai/chat/', views.ai_chat_api, name='ai_chat_api'),
 path('ai/chat/reset/', views.ai_chat_reset, name='ai_chat_reset')
] + [
 # django.conf.urls.static.static() silently returns [] when DEBUG=False, so every uploaded
 # image / resume 404'd in production. WhiteNoise only serves STATIC files, not MEDIA.
 re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), serve, {'document_root': settings.MEDIA_ROOT}),
]
