import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from users.forms import UserUpdateForm


def AccountUpdate(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Ita nia konta atualiza ona!')
			return redirect('user-account')
	else: u_form = UserUpdateForm(instance=request.user)
	context = {
		'u_form': u_form,
		'title': 'Konta', 'legend': 'Konta',
	}
	return render(request, 'auth/account.html', context)

class UserPasswordChangeView(PasswordChangeView):
	template_name = 'auth/change_password.html'
	success_url = reverse_lazy('user-change-password-done')

class UserPasswordChangeDoneView(PasswordResetDoneView):
	template_name = 'auth/change_password_done.html'