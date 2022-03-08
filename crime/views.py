from django.contrib.auth import authenticate, login, logout
from django.core.mail.message import EmailMessage
from django.shortcuts import redirect, render, get_object_or_404
from .models import Complaint, Contact, Evidencea, Evidenced, Evidencei, Evidencev, Feedback, Profile, UserProfile, Reply
from django.contrib.auth.decorators import login_required
from .forms import AbsUser, MyComplaint, MyContact, MyDev, MyEvidencea, MyEvidenced, MyEvidencei, MyEvidencev, MyFeed, MyProfile, MyReply, RegisterUserForm, Staff, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.urls import reverse
from .utils import token_generator
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Q
from datetime import datetime



# Create your views here.

#view for Terms and Conditons
@login_required(login_url='login')
def terms(request):
    return render(request, 'terms.html')

#view for Home Page or Landing Page
def index(request):
    return render(request, 'index.html')

#This is function for downloading profile pdf
@login_required(login_url='login')
def pdf(request, *args, **kwargs):
    pk = kwargs.get('pk')
    profile = get_object_or_404(Profile, pk=pk)

    template_path = 'pdf.html'
    context = {'profile': profile}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#function for downloading the complaint pdf
@login_required(login_url='login')
def complaintpdf(request, *args, **kwargs):
    pk = kwargs.get('pk')
    profile = get_object_or_404(Complaint, pk=pk)

    template_path = 'complaintpdf.html'
    context = {'profile': profile}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





#function for profile to show 
@staff_member_required(login_url='notallowed')
def staffviewprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    evid = Evidencev.objects.filter(user=pk)
    evida = Evidencea.objects.filter(user=pk)
    evidi = Evidencei.objects.filter(user=pk)
    evidd = Evidenced.objects.filter(user=pk)
    context = {'profile': profile, 'evid': evid, 'evida': evida, 'evidi': evidi, 'evidd':evidd}
    return render(request, 'staffviewprofile.html', context)


#function for Complaints

@login_required(login_url='login')
def complaint_view(request):
    
    form1 = Complaint.objects.all()
    return render(request, 'complaints.html', {'compla': form1})


#function for search profile by user(department)
@login_required(login_url='login')
def search(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else''
    profiles = Profile.objects.filter(id__icontains=q)
    context = {'profiles': profiles}
    return render(request, 'search.html', context)





def notallowed(request):
    return render(request, 'notallowed.html')





#function for creating a profile form
@staff_member_required(login_url='notallowed')
def profile_form(request):
    form = MyProfile()
    if request.method == "POST":
        form = MyProfile(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            idn = idgen(idn= "idn")
            obj.id = int(idn)
            obj.save()
          
            return redirect('search')
    else:
        messages.error(request, 'An error Occured During Registration')
        form = MyProfile()
    return render(request, 'profile_form.html', {'form': form })


#function for registration of staff
@staff_member_required(login_url='notallowed')
def staff_register(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Staff(request.POST)
            if form.is_valid():
                user = form.save(commit=False) 
                user.is_active = True
                user.is_staff = True
                idn = idgen(idn="idn")
                user.id = int(idn)
                form.save()
                email = user.email
                domain = get_current_site(request).domain

                email_subject = 'Reset Your Password (Required To Access Your Account)'
                email_body = '\nHi ' + user.username + ' You have been Succesfully Registered With Us \n\nThank You For Joining Us \n\nSteps To Reset Your Pass word: \n\n1. Click On This Link '+domain+'/reset_password \n\n2. Enter Your E-Mail Gven at Time of Registration '+email+'\n\n3. Click on the link Sent To Your E-Mail \n\n4. Reset Your Password \n\n5. Login To Your Account \n\nNow You are All Set...!! \n\nHappy Working ' '\n\nTeam '+ domain
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )

                email.send(fail_silently=False)
        else:
            form = Staff()
        return render(request, 'staff_register.html', {'form': form})
    else:
        return render(request, 'notallowed.html')
        

#function to Update the Profile_form

@staff_member_required(login_url='login')
def update_form(request, pk):
    profile = Profile.objects.get(id=pk)
    form = MyProfile(instance=profile)
    if request.method == 'POST':
        form = MyProfile(request.POST, instance = profile)
    if form.is_valid():
        form.save()
        return redirect('search')
    context = {'form': form}
    return render(request, 'profile_form.html' , context)



#function to Delete the Profile
@login_required(login_url='login')
def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()   
        return redirect('staffsearch')
    return render(request, 'delete.html', {'obj': profile})

# function for user search
@login_required(login_url='login')
def usersearch(request):
    return render(request, 'usersearch.html')

def result(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else''
    profiles = Profile.objects.filter(Q(id__icontains=q))
    number1 = profiles.count()
    context = {'profiles': profiles, 'number1':number1}
    return render(request, 'result.html', context)


# function for staff search 
@staff_member_required(login_url='login')
def staffsearch(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else''
    profiles = Profile.objects.filter(Q(firstname__icontains=q) | Q(id__icontains=q) | Q(lastname__icontains=q))
    number1 = profiles.count()
    context = {'profiles': profiles, 'number1':number1}
    return render(request, 'staffsearch.html', context)

#function for user to view their profile
@login_required(login_url='login')
def userview(request, pk):
    form = Profile.objects.get(id=pk)
    context = {'profile': form}
    return render(request, 'userview.html', context)

# function for profile staff
@staff_member_required(login_url='login')
def profilestaffuser(request):
    form = UserProfile.objects.all()
    context = {'form' : form }
    return render(request, 'profilestaffuser.html', context)

import random
def idgen(idn):
    number = "0123456789"
    string = number
    lenght = 8
    idn = "".join(random.sample(string, lenght))
    return idn


#function for Complaint page
@login_required(login_url='login')
def complaint(request):
    form = MyComplaint(request.POST or None, request.FILES or None)
    if request.method =='POST':
          
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.user = request.user
            idn = idgen(idn="idn")
            obj.id = int(idn)
            obj.save()
            email = obj.email
            now = datetime.now()
            comid = str(obj.id)
            date = str(now)
            domain = get_current_site(request).domain

            email_subject = 'Your Complaint Has Succesfully Registered With ' + domain
            email_body = '\nHi ' + obj.firstname + ' \nYou have Registered a Complaint on '+ date +' So The Complaint has Been Viewed By Our Staff \nYou will Be Informed With The Complaint Status Soon \nAnd Your Complaint ID is '+ comid +' You can Download A Complaint Copy From '+ domain + ' \nThankYou Team '+ domain 
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email],
            )

            email.send(fail_silently=False)
            return redirect('complaint_view')
        else:
            form = MyComplaint()
    return render(request, 'complaint.html' , {'form': form})


def evi(request, pk):
    form0 = MyEvidencea()
    form1 = MyEvidenced()
    form2 = MyEvidencei()
    form3 = MyEvidencev()
    if request.method == 'POST':
        form = MyEvidencea(request.POST, request.FILES)
        files = request.FILES.getlist('evidence_audio')
        if form.is_valid():
            for f in files:
                obj = Evidencea(evidence_audio = f)
                obj.user = Profile.objects.get(id=pk)
                obj.save()


        form = MyEvidencei(request.POST, request.FILES)
        files = request.FILES.getlist('evidence_img')
        if form.is_valid():
            for f in files:
                obj = Evidencei(evidence_img = f)
                obj.user = Profile.objects.get(id=pk)
                obj.save()


        form = MyEvidencev(request.POST, request.FILES)
        files = request.FILES.getlist('evidence_video')
        if form.is_valid():
            for f in files:
                obj = Evidencev(evidence_video = f)
                obj.user = Profile.objects.get(id=pk)
                obj.save()

        form = MyEvidenced(request.POST, request.FILES)
        files = request.FILES.getlist('evidence_doc')
        if form.is_valid():
            for f in files:
                obj = Evidenced(evidence_doc = f)
                obj.user = Profile.objects.get(id=pk)
                obj.save()

        return redirect('upl')
        
    context = {'form0': form0, 'form1': form1, 'form2': form2, 'form3':form3}
    return render(request, 'evi.html', context)

def upl(request):
    return render(request, 'upl.html')

def eviview(request):
    form = Evidencea.objects.all()
    context = {'form': form}
    return render(request, 'eviview.html', context)



# function for staffprofile

@staff_member_required(login_url='login')
def staffprofile(request):
    form = MyProfile()
    if request.method == "POST":
        form = MyProfile(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.id = int(idgen(idn="idn"))
            obj.save()
            no = obj.id
            email = obj.email
            aemail = obj.accuser_email
            caseid = str(obj.id)
         
            domain = get_current_site(request).domain

            email_subject = 'About Case You Registered With ' + domain
            email_body = '\nHi '+ obj.firstname + '\n\nYou Have Received This E-Mail Regarding About The Case You Have Registered Against '+obj.accuser_firstname+' \n\nSo We Want to Tell You That This Case Has Been Investigating \n\nYou Need to Visit Your Nearest Law Enforcement Agency For More Infomation \nThanks For Your Co-operation '+ '\nTeam ' + domain+'\nYou can visit '+ domain +' And See Your Case Nature And Your Case ID is '+ caseid +' \nYou Can Download a Profile Copy From There'
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email],
            )
            try:
                 email.send(fail_silently=False)
            except:
                messages.error(request, 'E-Mail Cannot be sent......!! Please Check Your Internet Connection')
           

            email_subject = 'This E-Mail is Regarding About a Case Registered Against You'
            email_body = 'Hi '+ obj.accuser_firstname + ' You have Receiving This E-Mail Because \nMr/Mrs/Miss : \n' + obj.firstname + ' \nHas Registered A Case Aginst You So You Need To Visit Your Nearest Law Enforcement Agency For More Information \nThank You for Your Co-Operation\nTeam '+ domain +'\nYou can visit '+ domain +' And See Your Case Nature And Your Case ID is\n'+ caseid +' \nYou Can Download a Profile Copy From There'

            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [aemail],
            )

            email.send(fail_silently=False)
            
            return render(request, 'next.html', {'no': no})
    else:
        form = MyProfile()
    return render(request, 'staffprofile.html', {'form': form} )


# function for Login the User

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does Not Exits')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('staff_register')
            else:
                if request.user.is_staff:
                    return redirect('staffdashboard')
                else:
                    return redirect('index')

        else:
            messages.error(request, 'Username or Password Does not Exits')
             
    context = {}
    return render(request, 'login.html', context)


# fucntion for Logout the User
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('index')


#function for Registrations

def registerPage(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.is_active = False  
            idn = idgen(idn="idn")
            user.id = int(idn)
            form.save()
            email = user.email
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
            
            activate_url = 'http://'+domain+link
            
            email_subject = 'Activate Your Account'
            email_body = 'Hi ' + user.username + ' Please Use This Link\n' + activate_url +'\nYou Need To Activate Your Account To Start Using The Web Site ThankYou '+domain
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email],
            )

            email.send(fail_silently=False)
  
            return redirect('sente')
    else:

        form = RegisterUserForm()
    return render(request, 'registerPage.html', {'form': form})

class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=id)

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated Succesfully')
            return redirect('login')

        except Exception as ex:
            pass
        return redirect('login')


#function for UserProfile 
@login_required(login_url='login')
def userProfile(request):
    return render(request, 'user_profile.html')

#function for pagenot found

def page_not(request):
    return render(request, 'page_not.html')

#function for E-Mail Succefully sent
def sente(request):
    return render(request, 'sente.html')

#Function for updating userprofile

@login_required(login_url='login')
def editprofile(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            

    return render(request, 'editprofile.html', {'form': form})


#function for staff Dashboard

@staff_member_required(login_url='login')
def staffdashboard(request):
    form = Complaint.objects.all()
    number = form.count()
    prof = Profile.objects.all()
    profn = prof.count()
    user1 = User.objects.all()
    user2 = user1.count()
 
    return render(request, 'staffdashboard.html', {'compla': number, 'profn': profn, 'user2': user2 , 'form': form, 'prof': prof})


#function for staffcomplaint
@staff_member_required(login_url='login')
def staffcomplaint(request):
    form1 = Complaint.objects.all()
    return render(request, 'staffcomplaint.html', {'compla': form1})

@login_required(login_url='login')
def userextend(request):
    form = AbsUser()
    if request.method == "POST":
        form = AbsUser(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('profilestaffuser')
    else:

        context = {'form': form}
        return render(request, 'userextend.html', context)

@login_required(login_url='login')
def edituser(request, pk):
    pro = UserProfile.objects.get(id=pk)
    form = AbsUser(instance=pro)
    

    if request.method == 'POST':
        form = AbsUser(request.POST, request.FILES, instance=pro)
        if form.is_valid():
            form.save()
            return redirect('profilestaffuser')
        else:
            form = AbsUser(instance=pro)
    return render(request, 'edituser.html', {'form': form})


#function for staff edit profile
@staff_member_required(login_url='login')
def staffedit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = MyProfile(instance=profile)

    if request.method == 'POST':
        form = MyProfile(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('staffsearch')
        else:
            form = MyProfile(instance=profile)
    context = {'form': form , 'pro': profile}
    return render(request, 'staffprofileedit.html' , context)

#function for Contact and Feedback 
@login_required(login_url='login')
def contact(request):
    form = MyContact()
    if request.method == 'POST':
        form = MyContact(request.POST)
        if form.is_valid():
            obj = form.save()
            email = obj.email
            email_subject = 'ThankYou For Contacting Us'
            domain = get_current_site(request).domain

            email_body = ' Hi '+ obj.name + ' ThankYou For Contacting US Our Executive Will Be Contact You Soon...!! \nThankYou Team '+domain
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email],
            )
            email.send(fail_silently=False)
            return redirect('con')
    context = {'form': form }
    return render(request, 'contact.html', context)


# function for Feedback form 
@login_required(login_url='login')
def feedback(request):
    form = MyFeed()
    if request.method == 'POST':
        form = MyFeed(request.POST)
        if form.is_valid():
            obj = form.save()
            rate = int(obj.rating)
            if (rate<5):
                mes = 'We Will Try To Improve Our Services'
            else:
                mes = 'Great....!! ThankYou We Will Keep Up With Our Services'
            rate = str(obj.rating)

    

            email = obj.email
            email_subject = 'ThankYou For Your Feedback'
            domain = get_current_site(request).domain

            email_body = ' Hi '+ obj.name + ' ThankYou For Your Feedback You hava Rated '+ rate + ' ' + mes + ' \nThankYou Team '+domain
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email],
            )
            email.send(fail_silently=False)
            return redirect('thankyou')
    context = {'form' : form }
    return render(request, 'feedback.html', context)

#function for thanking
@login_required(login_url='login')
def thankyou(request):
    return render(request, 'thankyou.html')

#function for contacting thanking
@login_required(login_url='login')
def con(request):
    return render(request, 'cont.html')

@staff_member_required(login_url='notallowed')
def contactview(request):
    form = Contact.objects.all()
    context = {'form': form}
    return render(request, 'contactview.html', context)

@staff_member_required(login_url='notallowed')
def viewcontact(request, pk):
    form = Contact.objects.get(id=pk)
    context = {'form': form}
    return render(request, 'viewcontact.html', context)

@staff_member_required(login_url='notallowed')
def reply(request, pk):
    form = Contact.objects.get(id=pk)
    if request.method == 'POST':
        rep = MyReply(request.POST or None, request.FILES or None)
        if rep.is_valid():
            obj = rep.save(commit=False)
            email = form.email
            email_subject = 'Reply From Crime Management for Contacting Us'
            message = obj.message
            obj.save()
            now = datetime.now()
            date = str(now)
            domain = get_current_site(request).domain
            email_body = 'Hi We Are Replying You on '+ date + ' Beacuse You Tried To Contact Us \n\n'+ 'Message: \n\n '+ message +'\n\nTeam '+ domain
            email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )
            email.send(fail_silently=False)
            return redirect('sent')
    re = MyReply() 
    return render(request, 'reply.html', {'form': form, 're': re} )

@staff_member_required(login_url='notallowed')
def feedbackview(request):
    form = Feedback.objects.all()
    context = {'form': form}
    return render(request, 'feedbackview.html', context)

@staff_member_required(login_url='notallowed')
def viewfeedback(request, pk):
    form = Feedback.objects.get(id=pk)
    context = {'form': form}
    return render(request, 'viewfeedback.html', context)

@staff_member_required(login_url='notallowed')
def sent(request):
    return render(request, 'sent.html')

@staff_member_required(login_url='notallowed')
def next(request):
    return render(request, 'next.html')


@staff_member_required(login_url='notallowed')
def staffviewcomplaint(request, pk):
    form = Complaint.objects.get(id=pk)
    context = {'form': form}
    return render(request, 'staffviewcomplaint.html', context)

@staff_member_required(login_url='notallowed')
def replycomplaint(request, pk):
    form = Complaint.objects.get(id=pk)
    if request.method == 'POST':
        rep = MyReply(request.POST or None, request.FILES or None)
        if rep.is_valid():
            obj = rep.save(commit=False)
            email = form.email
            id = str(form.id)
            email_subject = 'Reply from Crime Management System Regarding Your Complaint'
            message = obj.message
            obj.save()
            now = datetime.now()
            date = str(now)
            domain = get_current_site(request).domain
            email_body = "we replying to you regarding about the Complaint You Reported ID "+ id +"\n" + message + "\nThank You\n"+ date + "  " +domain
            email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )
            email.send(fail_silently=False)
            return redirect('sent')
    re = MyReply() 
    return render(request, 'replycomplaint.html', {'form': form, 're': re} )


def developers(request):
    form = MyDev()
    if request.method == 'POST':
        form = MyDev(request.POST)
        if form.is_valid():
            obj = form.save()
            message = obj.message
            email = obj.email
            name = obj.name
            email_subject = 'Some One Has Contacted You...!!'
            semail = 'shivu11022002@gmail.com'
            domain = get_current_site(request).domain
            email_body ="Message:\n\n"+ message + "\n\nFrom : \n"+"Name: "+ name +"\nE-Mail: "+ email + "\nThankYou "+domain
            email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [semail],
                )
            email.send(fail_silently=False)

            email = obj.email
            message = "Thanks For Visiting Our Web Application Feel Free To Try It , To Explore it and Contribute To It \nYou Will Be Answered Back By Developers \nThankYou \nTeam Developers | Crime Management System"
            subject = "We Will Reach You Soon ....!!!"
            email = EmailMessage(
                subject,
                message,
                'noreply@email.com',
                [email],
            )
            email.send(fail_silently=False)
        else:
            return HttpResponse('SomeThing Error Occured....!!!')
    return render(request, 'developers.html' ,{'form': form})