from django.shortcuts import render

# Create your views here.
def cards(request):
    return render(request, "user_cards.html")

def words(request):
    return render(request, "selected_card.html")