from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from project.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task4/', include('task4.urls')),
    path('blog/', include('blog.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]
