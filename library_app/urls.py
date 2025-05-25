from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, IssuedBookViewSet


router = DefaultRouter()
router.register('books' ,BookViewSet)
router.register('member' ,MemberViewSet)
router.register('issued' ,IssuedBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]