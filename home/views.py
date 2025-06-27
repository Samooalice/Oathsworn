from django.shortcuts import render

def home(request):
    chapters = range(1, 22)  # 1~21
    return render(request, 'home.html', {'chapters': chapters})
