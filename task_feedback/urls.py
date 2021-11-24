from django.urls import path

from .views import DepPayView, DepPayList,DepPayUpdate

urlpatterns = [
    path('deppay/', DepPayView.as_view()),
    path('deppay_list/', DepPayList.as_view()),
    path('deppay/<int:pk>', DepPayUpdate.as_view()),

]