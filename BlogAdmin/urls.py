from django.urls import path
from . import views

urlpatterns = [

    path('v1/', views.index, name='index'),
    # path('', views.index, name='index'),
    path('test1',views.test,name = "test"),
    path('detail',views.detail_data)
    ]
