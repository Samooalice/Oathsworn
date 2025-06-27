from django.shortcuts import render

def chapter_detail(request, number):
    return render(request, 'chapter_detail.html', {'chapter_number': number})
