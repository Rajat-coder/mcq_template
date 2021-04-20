from django.urls import path
from authentication.views import *

urlpatterns=[
    path("",base),
    path("online/exam/",ExamOnlineView,name="onlineexam"),
]