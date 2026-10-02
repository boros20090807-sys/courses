from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    register, login, logout,
    CourseViewSet, LessonViewSet, HomeworkViewSet, CommentViewSet
)

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('homeworks', HomeworkViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', include(router.urls)),
]