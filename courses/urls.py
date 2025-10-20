from django.urls import path
from courses.views import CourseAddView, CourseListView, CourseDeleteView, CourseUpdateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/add-course/', CourseAddView.as_view(), name='add-course'),
    path('courses/<uuid:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<uuid:id>/update/', CourseUpdateView.as_view(), name='update-course'),
    path('courses/<uuid:id>/delete/', CourseDeleteView.as_view(), name='delete-course'),
]
