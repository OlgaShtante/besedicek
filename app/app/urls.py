from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users.views import user_detail
from register.views import registration
from user_languages.views import languages, vocabulary
from user_cards.views import cards, words

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('register/', registration),
    path('users/', user_detail),
    path('user-languages/', languages),
    path('user-vocabulary/', vocabulary),
    path('user-cards/', cards),
    path('user-words/', words),
]