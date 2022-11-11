from django import forms
from .models import Event,EventDetail,EventRep,EventFdbck
from datetime import datetime

Choice_cat=[('Technical','Technical'),('E-Sports','E-Sports'),('Sports','Sports'),('Cultural','Cultural'),('','Others')]

class SubscribeForm(forms.ModelForm):
	id1=forms.IntegerField(widget=forms.HiddenInput())
	email=forms.EmailField(widget=forms.HiddenInput())

	class Meta:
		model = EventDetail
		fields = ("id1","email")

class AddEventForm(forms.ModelForm):
	name=forms.CharField(max_length=100,required=True)
	body=forms.CharField(max_length=65536,required=True, widget=forms.Textarea)
	date=forms.CharField(widget=forms.DateTimeInput, help_text="YYYY-MM-DD HH:MM")
	venue=forms.CharField(max_length=50,required=True)
	link=forms.CharField(max_length=75,required=True)
	contact=forms.CharField(max_length=100)
	added_on=forms.CharField(widget=forms.DateTimeInput,disabled=True,initial=datetime.now())
	category=forms.ChoiceField(widget=forms.RadioSelect,choices=Choice_cat)
	email=forms.EmailField(required=True)

	class Meta:
		model=Event
		fields=("name","body","date","venue","link","contact","added_on","category","email")

class AddReport(forms.ModelForm):
	name=forms.CharField(required=False, widget=forms.HiddenInput)
	report=forms.CharField(max_length=65536,required=True, widget=forms.Textarea)
	added_on=forms.CharField(widget=forms.DateTimeInput,disabled=True, initial=datetime.now())

	class Meta:
		model=EventRep
		fields=("name","report","added_on")

class AddFeedback(forms.ModelForm):
	name=forms.CharField(required=True, widget=forms.HiddenInput)
	email=forms.EmailField(widget=forms.HiddenInput)
	feedback=forms.CharField(max_length=65536,required=True, widget=forms.Textarea)
	added_on=forms.CharField(widget=forms.DateTimeInput,disabled=True,initial=datetime.now())
	uname=forms.CharField(widget=forms.HiddenInput,required=True)

	class Meta:
		model=EventFdbck
		fields=("name","email","feedback","added_on","uname")