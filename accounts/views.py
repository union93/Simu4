from .models import User
from django.shortcuts import render, redirect
from django.contrib import auth

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.object.create_user(
                email=request.POST['email'],
                password=request.POST['password1'],
                nickname=request.POST['nickname'],
            )
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/signup/user_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "건국시무 가입확인 메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
        return redirect("home")  # 홈화면 리디렉션
    return render(request, 'accounts/signup/signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')  # 홈화면 리디렉션
        else:
            return render(request, 'accounts/login/login.html', {'error': '이메일 혹은 비밀번호가 불일치 합니다.'})
    else:
        return render(request, 'accounts/login/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request,'accounts/login/login.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.object.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('home')  # 홈화면 리디렉션
    else:
        return render(request, 'home', {'error': '계정 활성화 오류'})
    return
