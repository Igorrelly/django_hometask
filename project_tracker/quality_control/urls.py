from django.urls import path
from quality_control import views
from .views import *

app_name = 'quality_control'

CBV_urls = True


if CBV_urls:
    urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('bugs/', views.BugReportListView.as_view(), name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('bugs/add_bug_report/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='bug_update'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='bug_delete' ),   
        
    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
    path('features/add_feature_request', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
    path('features/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='feature_update'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='feature_delete'),
    ]
else:
    urlpatterns = [
    path('', views.index, name = 'index'),

    path('bugs/', views.bug_list, name='bug_list'),  # Баги
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'), # Детали багов
    path('bugs/create_bug_report/', views.create_bug_report, name='create_bug_report'),
    path('bugs/<int:bug_id>/update/', views.bug_update, name='bug_update'),
    path('bugs/<int:bug_id>/delete/', views.bug_delete, name='bug_delete' ),

    path('features/', views.feature_list, name='feature_list'), # Улучшения    
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'), # Детали улучшений    
    path('features/create_feature_request/', views.create_feature_request, name='create_feature_request'),
    path('features/<int:feature_id>/update/', views.feature_update, name='feature_update'),
    path('features/<int:feature_id>/delete/', views.feature_delete, name='feature_delete'),
    ]
