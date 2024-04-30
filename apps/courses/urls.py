from django.urls import path
from apps.courses.views import CourseListView, EnrollCourseView

urlpatterns = [
    path('', CourseListView, name='course_list'),
    path('enroll/<int:course_id>/', EnrollCourseView, name='enroll_course'),
]