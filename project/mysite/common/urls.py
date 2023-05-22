from django.urls import path
# 사용자 인증에 관한 모듈
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

# 로그인 했을 때 어떤 화면을 띄울 것인지.
# 또한 아래 함수들을 이용해서 로그인에 관한 view를 만들지 않아도 된다.
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
