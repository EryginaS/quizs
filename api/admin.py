from django.contrib import admin
from .models import Quiz, Question, Answer, Radio
from leaflet.admin import LeafletGeoAdmin


class QuizAdmin(LeafletGeoAdmin):
    list_display = ('name', 'locate')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Radio)