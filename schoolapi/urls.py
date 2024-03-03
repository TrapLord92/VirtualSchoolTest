from django.urls import re_path as url,include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet,basename='course')

urlpatterns = [
    url('views/', views.SubjectListView.as_view(), name='subject_list'),
    url('detail/', views.SubjectDetailView.as_view(), name='subject_detail'),
    url(r'^', include(router.urls)),
    
]
    
    

    