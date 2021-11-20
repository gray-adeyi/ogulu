from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('message/',views.MessageView.as_view(), name='message'),
    path('projects/<int:pk>/', views.Portfolio.as_view(), name='portfolio'),
]
