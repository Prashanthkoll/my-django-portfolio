from django.urls import path
from . import views
urlpatterns = [
    path('pub',views.pub,name='pub'),
]