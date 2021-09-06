from rest_framework.generics import ListAPIView
from polls.models import Category, Questions, Choice, Result
from .serializers import FanSerializer, SavolSerializer, JavobSerializer, NatijaSerializer


class SubAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = FanSerializer


class QuizAPIView(ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = SavolSerializer


class AnsAPIView(ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = JavobSerializer


class ResAPIView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = NatijaSerializer
