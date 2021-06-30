from django.shortcuts import render
from polls.models import Questions, Choice, Category


def index(request):
    fanlar = Category.objects.all()
    return render(request, 'polls/index.html', {'fanlar': fanlar})


def savollar(request, category_id):
    savol = Category.objects.get(pk=category_id)
    all_savollar = Questions.objects.filter(category=savol)
    return render(request, 'polls/questions.html', {'all_savollar': all_savollar, })


