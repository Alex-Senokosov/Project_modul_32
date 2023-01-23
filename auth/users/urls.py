from django.urls import path
from .views import RegisterView,LogininView,UserView,Logout
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LogininView.as_view()),
    path('user', UserView.as_view()),
    path('Logout', Logout.as_view()),

]
