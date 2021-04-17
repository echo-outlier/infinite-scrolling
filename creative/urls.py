from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="creative_index"),
    path('lorem/<int:word>',views.random,name="lorem"),
    path('loremtext',views.loremtext,name="loremtext")
]
