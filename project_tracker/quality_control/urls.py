from django.contrib import admin
from django.urls import path, include

from quality_control import views

app_name='quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bugs'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/', views.feature_list, name='features'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail')
]
