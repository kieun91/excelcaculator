from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def signup(request):
    return render(request, "main/signup.html")

def signin(request):
    return render(request, "main/signin.html")

def verifyCode(request):
    return render(request, "main/verifyCode.html")

def verify(request):  # 인증이 완료되면 메인 화면으로 보내줘
     return redirect('main_index')

def result(request):
    return render(request, "main/result.html")


def join(request):
    if request.method == 'POST':
        name = request.POST['signupName']
        email = request.POST['signupEmail']
        pw = request.POST['signupPW']

        # User 모델로 사용자 생성
        user = User.objects.create_user(username=name, email=email, password=pw)

        print("사용자 정보 저장 완료됨!")
        return redirect("main_verifyCode")
    else:
        # POST 요청이 아닌 경우에 대한 처리
        return render(request, "main/signup.html")  # 예: 재입력을 요청하는 페이지로 이동
