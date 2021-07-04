from django.shortcuts import render, HttpResponse
from polls.models import Questions, Choice, Category
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'polls/index.html'

    def index(self, **kwargs):
        fanlar = super().index(**kwargs)
        fanlar['fanlar':fanlar] = Category.objects.all()
        return fanlar

    def savollar(self, request, category_id):
        savol = Category.objects.get(pk=category_id)
        all_savollar = Questions.objects.filter(category=savol)
        return render(request, 'polls/questions.html', {'all_savollar': all_savollar, })


    def check(request):
        answer = []
        questions_numb = []
        for key, value in request.GET.items():
            questions_numb.append(key)
            answer.append(int(value))

        questions_l = Questions.objects.filter(id__in=questions_numb)
        return render(request, 'polls/questions.html',
                      {'questions_l': questions_l,
                       'answer': answer})
