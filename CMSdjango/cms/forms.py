from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from cms.models import Course

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']
        labels={'email': 'Email'}
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']
        labels={'email': 'Email'}
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['CourseName', 'Desc', ]
        labels={'CourseName':'Course Name','Desc':'Description'}
        widgets={'CourseName':forms.TextInput(attrs={'class':'form-control'}),
        # 'CourseCredits':forms.IntegerField(attrs={'class':'form-control'}),
        # 'CourseImage':forms.ImageField(attrs={'class':'form-control'}),
        'Desc':forms.Textarea(attrs={'class':'form-control'}),
        # 'Tags':forms.TextInput(attrs={'class':'form-control'}),
        }
