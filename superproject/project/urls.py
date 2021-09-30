from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task4/', include('task4.urls')),
    path('blog/', include('blog.urls')),
    path('login/', LoginView.as_view()),
    ]
