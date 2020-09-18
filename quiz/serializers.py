from rest_framework import serializers
from .models import Quiz

# model을 json으로 변환
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title','body', 'answer')
    
