from django.urls import path
from . import views

# app_nameはテンプレートからURLを参照する場合の名前空間となる
# 例えば detail は <a href="{% url 'polls:detail' question.id %}">...</a> のように参照できる
app_name = "polls"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.detail, name="results"),
    path('<int:question_id>/vote/', views.detail, name="vote"),
]
