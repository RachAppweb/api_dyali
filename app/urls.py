from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('posts',views.PoststView,basename='posts')
router.register('comment',views.CommentView,basename='comment')
urlpatterns = [
    path('user/posts/', views.get_user_posts,name='user_posts'),
]
urlpatterns+=router.urls