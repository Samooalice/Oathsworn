from django.shortcuts import render

# Create your views here.
def home(request):
    popup_message = "환영합니다! 홈페이지에 오신 것을 환영합니다."
    return render(request, "home.html", {"popup_message": popup_message})