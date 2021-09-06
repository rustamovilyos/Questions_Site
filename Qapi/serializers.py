from polls.models import Questions, Choice, Category, Result
from rest_framework import serializers


class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category, Questions, Choice, Result
        fields = '__all__'


class SavolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class JavobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class NatijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
