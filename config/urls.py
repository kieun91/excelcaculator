from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('main.urls'), name = "main"),
    path('email/', include('sendEmail.urls'), name="email"),
    path('calculate/', include('calculate.urls'), name="calculate"),
]