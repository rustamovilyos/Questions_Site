from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('site_api/', include('Qapi.urls'), name='site_api'),
]
