from django.shortcuts import render, HttpResponse
from polls.models import Questions, Choice, Category, Result
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(ListView):
    model = Category
    template_name = "polls/index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class ResultListView(ListView):
    template_name = 'polls/user_account.html'

    def get_queryset(self):
        return Result.objects.filter(users=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResultListView, self).dispatch(request, *args, **kwargs)


@login_required
def savollar(request, category_id):
    savol = Category.objects.get(pk=category_id)
    all_savollar = Questions.objects.filter(category=savol)
    return render(request, 'polls/questions.html', {'all_savollar': all_savollar, })


@login_required
def check(request):
    user = request.user
    answer = []
    questions_numb = []
    for key, value in request.GET.items():
        questions_numb.append(key)
        answer.append(int(value))

    questions_l = Questions.objects.filter(id__in=questions_numb)
    choices = Choice.objects.filter(id__in=answer)

    correct_answers = 0
    for ch in choices:
        if ch.correct:
            correct_answers += 1
    result = (correct_answers / len(answer) * 100)

    Result.objects.update_or_create(
        users=user, subject=questions_l[0].category,
        defaults={
            'users': user,
            'subject': questions_l[0].category,
            'result': result
        },
    )

    return render(request, 'polls/result.html',
                  {'questions_l': questions_l,
                   'answer': answer,
                   'result': result
                   })



