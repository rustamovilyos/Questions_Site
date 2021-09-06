from django.urls import path
from polls.views import IndexView, savollar, check, ResultListView
app_name = 'polls'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('questions/<int:category_id>/', savollar, name='questions'),
    path('check/', check, name='check'),
    path('user_account/', ResultListView.as_view(), name='user_account'),
]