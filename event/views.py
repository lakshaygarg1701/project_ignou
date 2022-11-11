from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.views.generic.edit import FormView
from .models import Event, EventDetail, EventRep, EventFdbck
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import SubscribeForm,AddEventForm, AddReport, AddFeedback
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
class Data(ListView):
	model=Event
	template_name="list1.html"
	
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context
	
	def get_queryset(self):
		queryset=Event.objects.all()
		# queryset = queryset.filter(date__gte=datetime.today)
		category = self.request.GET.get('category' or None)
		dept=self.request.GET.get('department' or None)

		if dept:
			queryset = queryset.filter(dept__iexact=dept)

		if category:
			if category=='Others':
				queryset=queryset.filter(category__iexact="")
			else:
				queryset = queryset.filter(category__iexact=category)
		# queryset = queryset.filter(date__gte=datetime.today())
		queryset = queryset.order_by("date")
		render(self.request, 'list1.html')
		return queryset;

class Data_past(ListView):
	model=EventRep
	template_name="list2.html"
	
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context
	
	def get_queryset(self):
		queryset=EventRep.objects.all()
		# queryset = queryset.filter(date__gte=datetime.today)
		category = self.request.GET.get('category' or None)
		dept=self.request.GET.get('department' or None)

		if dept:
			queryset = queryset.filter(dept__iexact=dept)

		if category:
			if category=='Others':
				queryset=queryset.filter(category__iexact="")
			else:
				queryset = queryset.filter(category__iexact=category)

		queryset = queryset.order_by("date")
		render(self.request, 'list2.html')
		return queryset;


class Details(DetailView):
	model=Event
	template_name="detail.html"

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		pk=self.kwargs['pk']
		obj = get_object_or_404(Event,pk=pk)
		print(context)
		render(self.request,'detail.html')
		return context

class Details_past(DetailView):
	model=EventRep
	template_name="detail_past.html"
	queryset=EventRep.objects.all()

	def get_context_data(self,**kwargs):
		context=super(Details_past, self).get_context_data(**kwargs)
		pk=self.kwargs['pk']
		obj = get_object_or_404(EventRep,pk=pk)
		context['feedback']=EventFdbck.objects.filter(name=context['eventrep'].name)
		print(context, context['eventrep'].name)
		render(self.request, 'detail_past.html')
		return context

class Add(FormView):
	model=Event
	template_name="add.html"
	form_class=AddEventForm

	@login_required
	def post(self,request,*args,**kwargs):
		form = AddEventForm(request.POST or None)
		form.added_on=datetime.now()
		if form.is_valid(): # All validation rules pass
			form.save()
			return redirect('/content/upcoming',permanent=True)
		return render(self.request, 'add.html', {'form': form})

class AddRep(FormView):
	model=EventRep
	template_name="add.html"
	form_class=AddReport

	def post(self,request,*args,**kwargs):
		form = AddReport(request.POST or None)
		form.added_on=datetime.now()
		print(form.data['report'])
		if form.is_valid(): # All validation rules pass
			change=EventRep.objects.get(id1=kwargs['pk'])
			change.report=form.data['report']
			change.save()
			return redirect('list',permanent=True)
		return render(self.request, 'add.html', {'form': form})


class AddFdbck(FormView):
	model=EventFdbck
	template_name="add.html"
	form_class=AddFeedback

	def post(self,request,*args,**kwargs):
		request.POST._mutable=True
		form = AddFeedback(request.POST or None)
		form.added_on=datetime.now()
		change=EventRep.objects.get(id1=kwargs['pk'])
		form.data['name']=change.name
		form.data['email']=request.user.email
		form.data['uname']=request.user.username
		print(form.data['feedback'])
		if form.is_valid(): # All validation rules pass
			form.save()
			return redirect('list',permanent=True)
		return render(self.request, 'add.html', {'form': form})

class subscribe(FormView):
	model=EventDetail
	form_class=SubscribeForm
	template_name="newsletter.html"


	def post(self,request,*args,**kwargs):
		pk=kwargs['pk']
		form = SubscribeForm(request.POST or None) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			return redirect('list',permanent=True)
		return render(self.request, 'newsletter.html', {'form': form})