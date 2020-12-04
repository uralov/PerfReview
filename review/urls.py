from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='index'),
    path('<int:pk>/', views.CreateReviewView.as_view(), name='create'),
]
