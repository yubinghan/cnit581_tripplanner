from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.hm, name='hm'),
    path('register', views.rg, name='rg'),
    path('list', views.ls, name='ls'),
    path('edit', views.ed, name='ed'),
    path('daily', views.dl, name='dl'),
    path('tripRecommendation', views.tripRecommendation, name='tripRecommendation'),
]