from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView

urlpatterns = [
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('profile/', views.profile, name='profile'),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
