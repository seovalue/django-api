# quiz.app 에 대한 url을 관리, myapi의 urls.py 는 전체 폴더에 대한 url을 관리

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
        path("hello/", helloAPI),
        path("<int:id>/", randomQuiz),
]
