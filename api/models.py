from django.db import models
from django.contrib.auth.models import User


class Radio(models.Model):
    """ Вариант ответа """
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос',related_name='radio' )
    radio_text = models.CharField(max_length=150, verbose_name="Текст для варианта ответа")

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"


class Answer(models.Model):
    """ Ответ """
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос', )
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Пользвоатель',)
    text_answer = models.TextField(null=True, blank=True, verbose_name='Текстовое поле для ответа на вопрос',)
    answer = models.ManyToManyField(Radio, blank=True, verbose_name='ответ пользователя',)
    
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Question(models.Model):
    """ Вопросы """

    TYPE = [
        (0, 'text'),
        (1, 'one'),
        (2, 'many'),
    ]

    question_text = models.CharField(max_length=500, verbose_name='Текст вопроса')
    question_type = models.IntegerField(default=0, choices=TYPE, verbose_name='Тип ответа на вопрос')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, verbose_name='Опрос', related_name="questions")
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Quiz(models.Model):
    """ Опросы """

    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание опроса')
    start_date = models.DateField(null=False, verbose_name='Дата старта')
    end_date = models.DateField(null=False, blank=False, verbose_name='Дата окончания')

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Оросы"
    