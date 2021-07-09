from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.ItemLists.as_view()),
    path('create/', views.ItemCreate.as_view()),
    path('delete/<int:id>', views.ItemDestroy.as_view()),
]
