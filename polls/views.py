from django.shortcuts import render, HttpResponse
from polls.models import Questions, Choice, Category


def index(request):
    fanlar = Category.objects.all()
    return render(request, 'polls/index.html', {'fanlar': fanlar})


def savollar(request, category_id):
    savol = Category.objects.get(pk=category_id)
    all_savollar = Questions.objects.filter(category=savol)
    return render(request, 'polls/questions.html', {'all_savollar': all_savollar, })


def check(request):
    r = ''
    print(request.GET)
    for key, value in request.GET.items():
        ch = Choice.objects.get(pk=value)
        print(key)
        print(value)
        print(Choice.objects.get(pk=value))
        if ch.correct == True:
            r = r + f"{ch.questions} <p style='color:green'><strong>{ch.text}</strong></p>"
        else:
            r = r + f"{ch.questions} <p style='color:red'>{ch.text}</p>"
    return HttpResponse(r)
