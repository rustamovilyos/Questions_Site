from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from polls.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('questions/<int:category_id>', IndexView.as_view(), name='questions'),
    path('check/', IndexView.as_view(), name='check')
]