from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LandingPageViewSet, UserActivityViewSet, CreateMultipleUsersView, CreateMultipleUsersWithActivityView


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'landingpage', LandingPageViewSet)
router.register(r'useractivity', UserActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-multiple-users/', CreateMultipleUsersView.as_view(), name='create-multiple-users'),
    path('create-multiple-users-with-activity/', CreateMultipleUsersWithActivityView.as_view(), name='create-multiple-users-with-activity'),
]
