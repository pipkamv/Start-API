from django.urls import path
from .views import *

urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('article/<int:pk>', ArticleView.as_view())
]