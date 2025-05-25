from rest_framework.viewsets import ModelViewSet
from .models import Book,Member,IssuedBook
from .serializers import BookSerializer ,IssuedBookSerializer, MemberSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]

class IssuedBookViewSet(ModelViewSet):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return IssuedBook.objects.all()
        
        else:
            return IssuedBook.objects.filter(member__user = user)
        
    def perform_create(self, serializer):
        member = Member.objects.get(user = self.request.user)
        serializer.save(member = member)
    
    