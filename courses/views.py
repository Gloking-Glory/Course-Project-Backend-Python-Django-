from rest_framework import status, generics, permissions
from rest_framework.response import Response
from courses.models import Course
from .serializers import CourseSerializer, CourseListSerializer, CourseUpdateSerializer
from utils.pagination import PagePagination

class CourseAddView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            'message': 'Course created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Course.objects.all()
    pagination_class = PagePagination

    def get_queryset(self):
        queryset = super().get_queryset()
        course_title = self.request.query_params.get('course_title')
        university = self.request.query_params.get('university')

        if course_title and university:
            queryset = queryset.filter(
                course_title__icontains=course_title.strip(),
                university__icontains=university.strip()
            )
        elif course_title:
            queryset = queryset.filter(course_title__icontains=course_title.strip())
        elif university:
            queryset = queryset.filter(university__icontains=university.strip())
        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'courses': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'courses': serializer.data
        }, status=status.HTTP_200_OK)

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseUpdateSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        course_title = instance.course_title

        return Response({
            'message': f'Course "{course_title}" updated successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({
            'message': 'Course deleted successfully.'
        }, status=status.HTTP_200_OK)
