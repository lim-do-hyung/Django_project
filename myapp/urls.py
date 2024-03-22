from django.urls import path
from myapp import views
from graphene_django.views import GraphQLView
from myapp.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('',views.index), # views.index로 정의 했을 때 views.py의 index 함수와 연결해준다.
    # path('create/',views.create), # 이 경우는 create 함수와 연결 그리고 경로는 127.0.0.1:8000/create/ 경로로 지정  
    # path('read/<id>/',views.read), # <>내부의 인자를 파라미터로 받을 수 있다 만약 127.0.0.1:8000/read/14로 url를 입력했다면 14라는 인자를 받아서 함수에서 처리한다.
    # path('delete/',views.delete),
    # path('update/<id>/',views.update),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
