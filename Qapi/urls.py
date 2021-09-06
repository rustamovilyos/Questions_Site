from django.urls import path
from .views import SubAPIView, QuizAPIView, AnsAPIView, ResAPIView


urlpatterns = [
    path('', SubAPIView.as_view(), name='subAPI'),
    path('quiz', QuizAPIView.as_view(), name='quizAPI'),
    path('answer', AnsAPIView.as_view(), name='ansAPI'),
    path('result', ResAPIView.as_view(), name='resAPI'),
]
