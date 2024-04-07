from django.shortcuts import render

def user_detail(request):
    return render(request, "user_detail.html")