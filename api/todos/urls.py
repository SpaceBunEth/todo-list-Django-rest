from django.urls import path, include
from .views import TodoViewSet, CategoryViewSet #TodoAPIView,
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'todos', TodoViewSet)



urlpatterns = [
    # path('todo/', TodoAPIView.as_view()),
    # path('todo/<str:pk>/', TodoAPIView.as_view()), # capture our id
    path('', include(router.urls))
]