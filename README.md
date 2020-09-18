# RESTframework API

장고를 이용하여 간단한 RESTframework API를 만들어보았습니다.  
해당 api는 퀴즈 내용을 전달받도록 하는 api이며, 이 api로 전달되는 내용은 다음과 같습니다.👌

# API DOCS
BASE_URL : https://django-restframework-api.herokuapp.com/  

### 퀴즈 자료 가져오기
* URL    
METHOD: GET  
REQUEST URL: BASE_URL + /quiz/{number_of_quizes}

* RESPONSE  
```
{
        'title':'퀴즈 제목',
        'body':'퀴즈에 대한 답안 목록',
        'answer':퀴즈에 대한 정답
}
```


# 프로젝트의 배포
이 프로젝트는 실제 API 요청을 위해 `heroku`를 이용하여 배포되었습니다.  

# HOW TO RUN
```
git clone https://github.com/seovalue/django-restframework-api.git
cd django-restframework-api

# 가상환경에서 실행하십시오.
pip install -r requirements.txt
python manage.py runserver
```


# Contact
mathmjseo@khu.ac.kr
