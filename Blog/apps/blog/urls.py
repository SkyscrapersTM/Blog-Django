from django.urls import path
from .views import detailPost, home,general, programming, tecnology, tutorials, videogames

urlpatterns = [
    path('', home, name='index'),
    path('generales/',general, name = 'general'),
    path('programming/',programming, name = 'programming'),
    path('tecnology/',tecnology, name = 'tecnology'),
    path('tutorials/',tutorials, name = 'tutorials'),
    path('videogames/',videogames, name = 'videogames'),
    path('<slug:slug>', detailPost, name='detail-post'),
]
