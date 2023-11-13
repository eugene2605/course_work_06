from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView
import random
from string import ascii_letters, digits

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            password = ""
            for i in range(8):
                password += random.choice(list(ascii_letters + digits))
            new_user = form.save()
            new_user.verification_code = password
            new_user.is_active = False
            send_mail(
                'Подтвердите',
                f'Для подтверждения почты пройдите по ссылке http://127.0.0.1:8000/users/verification/{password}',
                settings.EMAIL_HOST_USER,
                [new_user.email]
            )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def mail_verification(verification_code):
    user = User.objects.get(verification_code=verification_code)
    if user is not None:
        user.is_active = True
        user.save()
    return redirect('users:login')


def password_recovery(request):
    if request.method == 'POST':
        new_password = ""
        for i in range(8):
            new_password += random.choice(list(ascii_letters + digits))
        email = request.POST.get('email')
        send_mail(
            'Новый пароль',
            f'Ваш новый пароль: {new_password}',
            settings.EMAIL_HOST_USER,
            [email]
        )
        user = User.objects.get(email=email)
        if user is not None:
            user.set_password(new_password)
            user.save()
    return render(request, 'users/recovery.html')


class UserListView(ListView):
    model = User


def user_toggle_activity(request, pk):
    user_item = get_object_or_404(User, pk=pk)
    if user_item.is_active:
        user_item.is_active = False
    else:
        user_item.is_active = True

    user_item.save()

    return redirect(reverse('users:list_user'))
