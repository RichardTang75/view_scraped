from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>/', views.ItemDetail.as_view()),
    path('want/', views.WantItemList.as_view()),
    path('act_want/', views.InteractWantItemList.as_view()),
    path('ignore/', views.IgnoreItemList.as_view()),
    path('want/<int:pk>/', views.WantItemDetail.as_view()),
    path('ignore/<int:pk>/', views.IgnoreItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)