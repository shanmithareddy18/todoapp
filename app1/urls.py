from django.urls import path
from .views import persondetailslist, marksdetailslist, persondetailsview, marksdetailsview, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='create-user'),

    path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),

    path('persondetails/', persondetailslist.as_view(), name='person-details'),
    path('person/<int:pk>/', persondetailsview.as_view(), name='persons-id'),

    path('marks/', marksdetailslist.as_view(), name='marks-details'),
    path('marks/<int:pk>/', marksdetailsview.as_view(), name='marks-id'),
]