from django.contrib import admin
from django.urls import path, include
from ..models import Quiz
from .views import (
   QuizListApiView, 
   QuizDetailApiView, 
   QuizCreateApiView, 
   QuizUpdateApiView, 
   QuizDeleteApiView,
   QuestionListApiView,
   QuestionDetailApiView,
   QuestionUpdateApiView,
   QuestionCreateApiView,
   QuestionDeleteApiView,
   RadioListApiView,
   RadioCreateApiView,
   ActivQuizApiView, 
   UserQuizsListView,
   AnswerCreateView
   )

urlpatterns = [
   path('quizs', QuizListApiView.as_view(), name='quizs'), 
   path('quizs/<int:pk>', QuizDetailApiView.as_view(), name='quiz_detail'), 
   path('quizs/create/', QuizCreateApiView.as_view(), name='quiz_create'), 
   path('quizs/update/<int:pk>/', QuizUpdateApiView.as_view(), name='quiz_update'), 
   path('quizs/delete/<int:pk>/', QuizDeleteApiView.as_view(), name='quiz_delete'), 

   path('quizs/<int:quiz_pk>/questions', QuestionListApiView.as_view(), name='questions'), 
   path('quizs/<int:quiz_pk>/questions/<int:pk>', QuestionDetailApiView.as_view(), name='question_detail'), 
   path('quizs/<int:quiz_pk>/questions/', QuestionCreateApiView.as_view(), name='question_create'), 
   path('quizs/<int:quiz_pk>/questions/<int:pk>/update/', QuestionUpdateApiView.as_view(), name='question_update'), 
   path('quizs/<int:quiz_pk>/questions/<int:pk>/delete/', QuestionDeleteApiView.as_view(), name='question_delete'), 

   path('quizs/<int:quiz_pk>/questions/<int:question_pk>/radio', RadioListApiView.as_view(), name='radio'), 
   path('quizs/<int:quiz_pk>/questions/<int:question_pk>/radio/create/', RadioCreateApiView.as_view(), name='radio_create'), 

   path('active_quiz', ActivQuizApiView.as_view(), name='active_quiz'),
   path('quizs/<int:id>/questions/<int:question_pk>/answers/', AnswerCreateView.as_view(), name='answer_create'),
   path('my_quizs', UserQuizsListView.as_view() , name='answer')

]
