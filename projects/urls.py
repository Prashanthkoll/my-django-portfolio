from django.urls import path
from . import views
urlpatterns = [
    path('proj',views.proj,name='proj'),
    path('shadi',views.Shadi,name='shadi'),
    path('netf',views.netf,name='netf')
]