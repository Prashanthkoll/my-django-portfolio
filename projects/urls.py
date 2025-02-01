from django.urls import path
from . import views
urlpatterns = [
    path('proj',views.proj,name='proj'),
]