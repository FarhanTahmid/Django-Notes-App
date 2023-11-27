from django.urls import path
from UserData import views
app_name='UserData'

urlpatterns = [
    path('',views.landingPage,name='landing_page'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('notes/<str:username>',views.notes_home,name='notes_home')
]
