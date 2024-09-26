"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, Hod_Views, Staff_Views, Student_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.Base),
    #login path
    path('', views.user_login, name='login'),
    path('dologin/', views.doLogin, name='dologin'),
    path('logout/', views.doLogout, name='logout'),

    #profile path
    path('profile/', views.Profile, name='profile'),
    path('profile_update/', views.ProfileUpdate, name='profile_update'),

    #Hod path
    path('hod/home', Hod_Views.Home, name='hod_home'),
    path('hod/student/add', Hod_Views.Add_Student, name='add_student'),
    path('hod/student/view', Hod_Views.View_Student, name='view_student'),
    path('hod/student/edit/<str:id>', Hod_Views.Edit_Student, name='edit_student'),
    path('hod/student/update/', Hod_Views.Update_Student, name='update_student'),
    path('hod/student/delete/<str:admin>', Hod_Views.Delete_Student, name='delete_student'),
    path('hod/student/add_course', Hod_Views.Add_Course, name='add_course'),
    path('hod/student/view_course', Hod_Views.View_Course, name='view_course'),
    path('hod/student/edit_course/<str:id>', Hod_Views.Edit_Course, name='edit_course'),
    path('hod/student/update', Hod_Views.Update_Course, name='update_course'),
    path('hod/student/delete/<str:id>', Hod_Views.Delete_Course, name='delete_course'),


    path('hod/staff/add/', Hod_Views.Add_Staff, name='add_staff'),
    path('hod/staff/view/', Hod_Views.View_Staff, name='view_staff'),
    path('hod/staff/edit/<str:id>', Hod_Views.Edit_Staff, name='edit_staff'),
    path('hod/staff/update', Hod_Views.Update_Staff, name='update_staff'),
    path('hod/staff/delete/<str:admin>', Hod_Views.Delete_Staff, name='delete_staff'),


    path('hod/subject/add', Hod_Views.Add_Subject, name='add_subject'),
    path('hod/subject/view', Hod_Views.View_Subject, name='view_subject'),
    path('hod/subject/edit/<str:id>', Hod_Views.Edit_Subject, name='edit_subject'),
    path('hod/subject/update/', Hod_Views.Update_Subject, name='update_subject'),
    path('hod/subject/delete/<str:id>', Hod_Views.Delete_Subject, name='delete_subject'),

    path('hod/session/add', Hod_Views.Add_Session, name='add_session'),
    path('hod/session/view', Hod_Views.View_Session, name='view_session'),
    path('hod/session/edit/<str:id>', Hod_Views.Edit_Session, name='edit_session'),
    path('hod/session/update/', Hod_Views.Update_Session, name='update_session'),
    path('hod/session/delete/<str:id>', Hod_Views.Delete_Session, name='delete_session'),
    path('hod/staff/send_notification', Hod_Views.Send_Notification, name = "send_notification"),
    path('hod/staff/save_notification', Hod_Views.Save_Notification, name = "save_notification"),


    #Staff Path
    path('staff/home', Staff_Views.Home, name='staff_home'),
    path('staff/notification', Staff_Views.Notification, name='notification'),
    path('staff/notification/mark_read/<str:status>', Staff_Views.Notification_Mark_Read, name='notification_mark_read'),
    

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
