from rest_framework.viewsets import ModelViewSet
from .models import Book,Member,IssuedBook
from .serializers import BookSerializer ,IssuedBookSerializer, MemberSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date

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

    @action(detail=False , methods=['get'] )
    def overdue(self, request):
        today = date.today()
        user = self.request.user
        if user.is_staff:
            overdue = IssuedBook.objects.filter(return_date__lt = today,returned=False)

        else:
            overdue = IssuedBook.objects.filter(
                return_date__lt = today,
                returned=False,
                member__user = user

                )
        serializer = self.get_serializer(overdue, many = True)
        return Response(serializer.data)
    
    @action(detail=True , methods=['post'], url_path='return')
    def return_book(self,request, pk=None):
        issue = self.get_object()
        issue_return_date = date.today()
        issue.returned = True
        issue.save()
        return Response ({'status':'Book Succesfully Returned'}) 
    