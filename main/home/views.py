from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate
from main.user.forms import CreateUserForm


def home(request):
	signupform = CreateUserForm()
	signinform = CreateUserForm()
	# if request.method == 'POST':
	# 	form = CreateUserForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 	else:
	# 		messages.error(request, form.errors)
	# 		print(form.errors)
	# 		return HttpResponse(json.dumps({'message': form.errors}))
	context = {'signupform': signupform, 'signinform': signinform}
	return render(request, "user/userentry.html", context)


def createuser(request):
	# form = CreateUserForm(request.POST)
	# print('method called', form.is_valid())
	# if form.is_valid():
	# 	form.save()
	# else:
	# 	return ValidationError(form.errors)
	context = {}
	if request.POST:
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			# email = form.cleaned_data.get('email')
			# raw_password = form.cleaned_data.get('password1')
			# account = authenticate(email=email, password=raw_password)
			# login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form
	
	else:
		form = CreateUserForm()
		context['registration_form'] = form