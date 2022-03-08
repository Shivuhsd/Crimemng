from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('complaint/', views.complaint, name='complaint'),
    
    path('complaint_view/', views.complaint_view, name = 'complaint_view'),

    path('usersearch/', views.usersearch, name='usersearch'), 

    path('result/', views.result, name='result'),
    
    #This view has some problem has to be solved 24/01/2022 17:21
    path('search/', views.search , name='search'),
    
    path('staffviewprofile/<str:pk>/', views.staffviewprofile, name='staffviewprofile'),

    path('userview/<str:pk>/', views.userview, name='userview'),
    
    #it has to be removed after Finalizing the Project 24/01/2022 17:22
    path('profile_form/', views.profile_form , name='profile_form'),
    
    path('update_form/<str:pk>/', views.update_form, name='update_form'),
    
    path('delete_profile/<str:pk>/', views.delete_profile, name='delete_profile'),
    
    path('login/', views.loginPage, name='login'),
   
    path('logoutUser/', views.logoutUser, name='logout'),
   
   #It has Some Bugs with Message Component Has to be solved 24/01/2022 17:24 pending 
    path('registerPage/', views.registerPage, name='registerPage'),
   
    #This page styling has to be improved and some work is needed 24/01/2022 17:25
    path('user_profile/', views.userProfile, name='userProfile'),
   

    path('page_not', views.page_not, name="page_not"),


    path('extend/', views.userextend, name='userextend'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="sent_succesfully.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="success.html"), name="password_reset_complete"),

    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name="activate"),

    path('sente/', views.sente, name='sente'),

    path('notallowed/', views.notallowed, name='notallowed'),

    path('staff_register', views.staff_register, name='staff_register'),

    path('pdf/<str:pk>/', views.pdf, name='pdf'),

    path('complaintpdf/<str:pk>/', views.complaintpdf, name='complaintpdf'), 

    #It has to be improved and some styling is needed 24/01/2022 17:26 pending 
    path('editprofile/', views.editprofile, name='editprofile'),

    path('staff_dashboard/', views.staffdashboard, name='staffdashboard'),

    path('staff_complaint/', views.staffcomplaint, name='staffcomplaint'),

    path('staff_profile/', views.staffprofile, name='staffprofile'),

    path('staff_search/', views.staffsearch, name='staffsearch'),

    path('profilestaffuser/', views.profilestaffuser, name='profilestaffuser'),

    path('staffedit_profile/<str:pk>/', views.staffedit_profile, name='staffedit_profile'),

    #Currently Working on it so needed to be done 24/01/2022 17:29 Completed 26/01/2022
    path('edituser/<str:pk>/', views.edituser, name='edituser'), 

    path('userextend/', views.userextend, name='userextend'),

    path('terms/', views.terms, name='terms'),

    path('contact/', views.contact, name='contact'),

    path('feedback/', views.feedback, name='feedback'),

    path('thankyou/', views.thankyou, name='thankyou'),

    path('con/', views.con, name='con'),

    path('contactview/', views.contactview, name='contactview'),

    path('viewcontact/<str:pk>/', views.viewcontact, name='viewcontact'),

    path('reply/<str:pk>/', views.reply, name='reply'),

    path('feedbackview/', views.feedbackview, name='feedbackview'),

    path('viewfeedback/<str:pk>/', views.viewfeedback, name='viewfeedback'),

    path('sent/', views.sent, name='sent'),

    path('evi/<str:pk>/', views.evi, name='evi'),

    path('eviview/', views.eviview, name='eviview'),

    path('next/', views.next, name='next'),

    path('upl/', views.upl, name='upl'),

    path('staffviewcomplaint/<str:pk>/', views.staffviewcomplaint, name='staffviewcomplaint'),

    path('replycomplaint/<str:pk>/', views.replycomplaint, name='replycomplaint'),

    path('developers/', views.developers, name="developers"),
]
