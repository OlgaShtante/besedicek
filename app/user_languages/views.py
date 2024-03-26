from django.shortcuts import render

def languages(request):
    return render(request, "user_languages.html")

def vocabulary(request):
    return render(request, "user_vocabulary.html")