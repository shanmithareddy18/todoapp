from django.urls import path
from .views import studentlist, courselist, studentview, courseview, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('register/', UserCreate.as_view(), name='create-user'),

    path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),

    path('students/', studentlist.as_view(), name='student-list'),
    path('students/<int:pk>/', studentview.as_view(), name='student-id'),

    path('courses/', courselist.as_view(), name='course-list'),
    path('courses/<int:pk>/', courseview.as_view(), name='course-id'),
]