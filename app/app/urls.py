from django.contrib import admin
from django.urls import path, include
from users.views import user_detail
from user_languages.views import languages, vocabulary
from user_cards.views import cards, words


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_detail),
    path('user-languages/', languages),
    path('user-vocabulary/', vocabulary),
    path('user-cards/', cards),
    path('user-words/', words),
]