from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('add_favorite/<str:quote>', views.add_favorite,name="add_favorite"),
]
