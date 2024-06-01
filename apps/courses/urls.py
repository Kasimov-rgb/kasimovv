from django.urls import path
from apps.courses.views import CourseListView, EnrollCourseView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('enroll/<int:course_id>/', EnrollCourseView.as_view(), name='enroll_course'),
]
