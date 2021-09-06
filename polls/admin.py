from django.contrib import admin
from polls.models import Questions, Category, Choice


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'questions', 'answer_text', 'correct')


admin.site.register(Questions)
admin.site.register(Category)
admin.site.register(Choice, ChoiceAdmin)
