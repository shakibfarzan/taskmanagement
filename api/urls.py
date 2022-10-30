from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
