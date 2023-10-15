
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail

from .models import (
	Liability, OweOver, CustomUser
)
from .forms import (
	CustomUserForm, LoginForm, LiabilityForm, OweForm
)


def send_email_to_owe_user(owe):
	subject = 'Owes Expenses'
	message = f'Hi {owe.user_owes.full_name}, you have total {owe.amount}  to give me.'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [owe.user_owes.email, ]
	send_mail( subject, message, email_from, recipient_list )


def index(request):
	return render(request, 'core/index.html', {})


def registration(request):
	form = CustomUserForm()

	if request.method == 'POST':
		form = CustomUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=True)
			user.set_password(form.data.get('password'))
			user.save()
			return redirect('user_login')
		return render(request, 'core/registration.html', {'form': form})
	return render(request, 'core/registration.html', {'form': form})


def login_form(request):
	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST.get('email')
			password = request.POST.get('password')
			user = authenticate(request, email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
		else:
			return render(request, 'core/login.html', {'form': form})
	return render(request,  'core/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('index')


def liability_form(request):
	form = LiabilityForm()

	if request.method == 'POST':
		form = LiabilityForm(request.POST)
		if form.is_valid():
			if not request.user.liability:
				liability = Liability.objects.create(
					user=request.user,
					expense=form.data.get('expense'),
					expense_type=form.data.get('expense_type'),
					spent_in_ownself=form.data.get('spent_in_ownself'),
				)
			return redirect('owe_form')
	else:
		return render(request, 'core/liability_form.html', {'form': form})
	return render(request, 'core/liability_form.html', {'form': form})


def owe_form(request):
	form = OweForm()

	if request.method == 'POST':
		form = OweForm(request.POST)
		if form.is_valid():
			owe_user = CustomUser.objects.get(id=form.data.get('user_owes'))
			owe = OweOver()
			owe.user_owes = owe_user
			owe.amount += int(form.data.get('amount'))
			owe.save()
			send_email_to_owe_user(owe)

			liability = Liability.objects.get(user=request.user)
			liability.owe_over.add(owe)
			liability.save()
			return redirect('owe_form')
	else:
		return render(request, 'core/owe_form.html', {'owe_form': form})
	return render(request, 'core/owe_form.html', {'owe_form': form})
