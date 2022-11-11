from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    roll_no=forms.CharField(max_length=11)
    mobile= forms.CharField(max_length=10)
    course=forms.CharField(max_length=10)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'roll_no', 'course', 'email', 'mobile', 'password1', 'password2')
  #   def save(self,*args,**kwargs):
		# conn=sqlite3.connect('../db.sqlite3')
		# crs=conn.cursor()
		# crs.execute('insert into user_detail values(?,?,?,?,?,?)',{username,first_name,last_name,mobile,roll_no,course})
		# conn.commit()
		# conn.close()