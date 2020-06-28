from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>/increase_score', views.increase_score, name='increase_score'),
    path('<int:pk>/decrease_score', views.decrease_score, name='decrease_score'),
    path('<int:pk>', views.show_word, name='show_word'),
]

