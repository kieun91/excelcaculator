from django.shortcuts import render

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