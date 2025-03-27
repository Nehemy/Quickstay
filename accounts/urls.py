from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<str:pk>/', PublicProfileView.as_view(), name='public-profile'),
    path('account/', ProfileDetailView.as_view(), name='account'),
    path('account/update/', AccountUpdateView.as_view(), name='account-update'),
    path('register/', SignUpView.as_view(), name='register'),
]
