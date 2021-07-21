from rest_framework import permissions, serializers 
from django.db.models import Q
from ..models import Question, Quiz, Radio, Answer


class QuizSerializer(serializers.ModelSerializer):
    """ Опрос/Опросы """
    
    class Meta:
        model = Quiz
        fields = ('__all__')


class QuizUpdateSerializer(serializers.ModelSerializer):
    """ Опрос/Опросы """
    
    class Meta:
        model = Quiz
        fields = ('end_date', 'description', 'name')


class QuizCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=3000)
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    class Meta:
        model = Quiz
        fields = ('__all__')


class QuestionSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(max_length=500)
    question_type = serializers.CharField(source='get_question_type_display')
    quiz = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Question
        fields = ('__all__')


class QuestionCreateSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(max_length=500)
    question_type = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ('question_text', 'question_type')


class RadioSerializer(serializers.ModelSerializer):
    radio_text = serializers.CharField(max_length=150)
    question = serializers.SlugRelatedField(slug_field='question_text', read_only=True)

    class Meta:
        model = Radio
        fields = ('__all__')


class RadioCreateSerializer(serializers.ModelSerializer):
    radio_text = serializers.CharField(max_length=150)

    class Meta:
        model = Radio
        fields = ('radio_text',)


class QuestionUserListSerializer(serializers.ModelSerializer):

    answers = serializers.SerializerMethodField('user_answers')

    class Meta:
        fields = ['question_text', 'answers']
        model = Question

    def user_answers(self, question):

        user_id = self.context.get('request').user.id
        answers = Answer.objects.filter(
            Q(question=question) & Q(user__id=user_id))
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data

class UserQuizSerializer(serializers.ModelSerializer):
    questions = QuestionUserListSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Quiz

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer


class PrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        question_id = self.context.get('request').parser_context['kwargs'][
            'question_pk']
        request = self.context.get('request', None)
        queryset = super(PrimaryKeyRelatedField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(question_id=question_id)


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['text_answer']
        model = Answer


class OneChoiceSerializer(serializers.ModelSerializer):
    answer = PrimaryKeyRelatedField(
        many=False,
        queryset=Radio.objects.all()
    )

    class Meta:
        fields = ['answer']
        model = Answer


class MultipleChoiceSerializer(serializers.ModelSerializer):
    answer = PrimaryKeyRelatedField(
        many=True,
        queryset=Radio.objects.all()
    )

    class Meta:
        fields = ['answer']
        model = Answer