from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import Complaint, Developer, Evidencei, Evidencea, Evidencev, Evidenced, Feedback, Profile, Reply, UserProfile, Contact
from django import forms
from django.contrib.auth.models import User

class MyDev(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Nickname'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '6'}),
        }

class MyFeed(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            'rating' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Rate From 1 to 9'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control', 'rows': '5'}),
        }
class MyContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control', 'rows': '5'}),
        }


class MyReply(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
        exclude = ('to',)

        widgets = {
            'message' : forms.Textarea(attrs={'class' : 'form-control', 'rows': '5'})
        }


class MyComplaint(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['firstname','lastname',"place", "phone","email", "pincode", "address","subject", "description", "photo", "file" ,"agree"]

        widgets = {
            'firstname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'place' : forms.TextInput(attrs={'class': 'form-control'}),
            'pincode' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'subject' : forms.Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'agree' : forms.CheckboxInput(attrs={'class' : 'form-check-input', 'checked':'checked', 'value': 'Agree To Our Terms'}),
}


class MyProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
        
       

        widgets = {
            'firstname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'place' : forms.TextInput(attrs={'class': 'form-control'}),
            'pincode' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'address' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'accuser_firstname' : forms.TextInput(attrs={'class': 'form-control'}),
            'accuser_lastname' : forms.TextInput(attrs={'class': 'form-control'}),
            'accuser_phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'accuser_pincode' : forms.TextInput(attrs={'class': 'form-control'}),
            'accuser_address' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'image_accuser' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'accuser_email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'fir' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'evidence' : forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}),
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}),
            
   
 
        }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class Staff(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


        widgets = {

            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        }


class AbsUser(ModelForm):
    class Meta:
        model = UserProfile
        fields='__all__'
        exclude = ('user',)

        widgets = {
            'bio' : forms.TextInput(attrs={'class' : 'form-control'}),
            'profile_pic' : forms.ClearableFileInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class MyEvidencei(ModelForm):
    class Meta:
        model = Evidencei
        fields= '__all__'
        exclude = ('user',)


        widgets = {
            'evidence_img' : forms.ClearableFileInput(attrs={'multiple': True, 'class' : 'form-control'}),
           
        }

class MyEvidencea(ModelForm):
    class Meta:
        model = Evidencea
        fields= '__all__'
        exclude = ('user',)


        widgets = {
        
            'evidence_audio' : forms.ClearableFileInput(attrs={'multiple': True, 'class' : 'form-control'}),
         
        }


class MyEvidencev(ModelForm):
    class Meta:
        model = Evidencev
        fields= '__all__'
        exclude = ('user',)


        widgets = {
        
            'evidence_video' : forms.ClearableFileInput(attrs={'multiple': True, 'class' : 'form-control'}),
           
        }


class MyEvidenced(ModelForm):
    class Meta:
        model = Evidenced
        fields= '__all__'
        exclude = ('user',)


        widgets = {
         
            'evidence_doc' : forms.ClearableFileInput(attrs={'multiple': True, 'class' : 'form-control'}),
        }