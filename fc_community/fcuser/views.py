from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

def index(request) : 
	res_data = {}
	user_id = request.session.get('user')
	if user_id :
		fcuser = Fcuser.objects.get(pk=user_id)
		res_data['user_id'] = fcuser
		
	return render(request, 'fcuser/index.html', res_data)

def logout(request) :
	if request.session.get('user') :
		del(request.session['user'])

	return redirect('/')

def login(request) :
	form = LoginForm()
	return render(request, 'fcuser/login.html', {'form': form})
	# if request.method == 'GET' : 
	# 	return render(request, 'fcuser/login.html')
	# elif request.method == 'POST' : 
	# 	username = request.POST.get('username', None)
	# 	password = request.POST.get('password', None)

	# 	res_data = {}

	# 	if not (username and password) :
	# 		res_data['error'] = '모든 값을 입력해주세요.'
	# 	else :
	# 		try :
	# 			fcuser = Fcuser.objects.get(username=username)
	# 			if check_password(password, fcuser.password) :
	# 				request.session['user'] = fcuser.id
	# 				return redirect('/')
	# 			else :
	# 				res_data['error'] = '비밀번호가 일치하지 않습니다.'
	# 		except Exception as e :
	# 			res_data['error'] = f'등록된 회원이 아닙니다. ({ e })'

	# 	return render(request, 'fcuser/login.html', res_data)


def register(request) : 
	if request.method == 'GET' : 
		return render(request, 'fcuser/register.html')
	elif request.method == 'POST' : 
		username = request.POST.get('username', None)
		useremail = request.POST.get('useremail', None)
		password = request.POST.get('password', None)
		re_password = request.POST.get('re-password', None)

		res_data = {}

		if not (username and useremail and password and re_password) :
			res_data['error'] = '모든 값을 입력해주세요.'
		elif password != re_password :
			res_data['error'] = '비밀번호가 다릅니다.'
		else :
			fcuser = Fcuser(
				username = username,
				useremail = useremail,
				password = make_password(password)
			)
			fcuser.save()

		return render(request, 'fcuser/register.html', res_data)