from datetime import datetime
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView,
)
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins, permissions
from django.db.models import Q
from ..models import Quiz, Question, Answer
from .serializers import (
    QuizSerializer, 
    QuizCreateSerializer, 
    QuestionSerializer, 
    QuestionCreateSerializer,
    RadioCreateSerializer,
    RadioSerializer,
    QuizUpdateSerializer,
    UserQuizSerializer,
    AnswerSerializer,
    TextSerializer,
    OneChoiceSerializer,
    MultipleChoiceSerializer
    )


class ActivQuizApiView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.filter(end_date__gte=datetime.today())


class QuizListApiView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.all()


class QuizDetailApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter()


class QuizCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuizCreateSerializer


class QuizUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuizUpdateSerializer
    http_method_names = ['patch', 'put']
    queryset = Quiz.objects.filter()


class QuizDeleteApiView(RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter()
       

class QuestionListApiView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_pk'])
        return quiz.questions.all()


class QuestionDetailApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_pk'])
        return quiz.questions.filter()


class QuestionCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionCreateSerializer

    def perform_create(self, serializer):
        quiz = get_object_or_404(Quiz, pk=self.kwargs['quiz_pk'])
        serializer.save(quiz=quiz)


class QuestionUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionCreateSerializer
    http_method_names = ['patch', 'put']

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_pk'])
        return quiz.questions.filter()

    def perform_update(self, serializer):
        quiz = get_object_or_404(Quiz, pk=self.kwargs['quiz_pk'])
        serializer.update(quiz=quiz)


class QuestionDeleteApiView(RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_pk'])
        return quiz.questions.filter()


class RadioListApiView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = RadioSerializer

    def get_queryset(self):
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'], quiz=self.kwargs['quiz_pk'])
        return question.radio.all()


class RadioCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = RadioCreateSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'], quiz=self.kwargs['quiz_pk'])
        serializer.save(question=question)
       

class AnswerCreateView(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            quiz__id=self.kwargs['id'],
        )
        if question.question_type == '0':
            return TextSerializer
        elif question.question_type == '1':
            return OneChoiceSerializer
        else:
            return MultipleChoiceSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            quiz__id=self.kwargs['id'],
        )
        serializer.save(user=self.request.user, question=question)


class UserQuizsListView(ListAPIView):
    serializer_class = UserQuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Quiz.objects.exclude(~Q(questions__answer__user__id=user_id))
        return queryset
        