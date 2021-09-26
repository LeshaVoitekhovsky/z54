from django.urls import path, include

from task4.views import task
from task4.views import ShowNumbersView

urlpatterns = [
    path('', task),
    path('info/', ShowNumbersView.as_view())
]