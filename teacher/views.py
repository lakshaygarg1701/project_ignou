from django.shortcuts import render, redirect
from .forms import FacultySignUp

# Create your views here.
def FacSignup(request):
	if request.method == 'POST':
		form = FacultySignUp(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			return redirect('home')
	else:
		form = FacultySignUp()
	return render(request, 'signup.html', {'form': form})