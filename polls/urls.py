from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from polls.views import index


urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:category_id>', views.savollar, name='questions')
]