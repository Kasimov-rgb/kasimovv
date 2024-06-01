from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from apps.courses.views import CourseListView


api_urlpatterns = [
    path('products/', include('apps.products.api.urls')),
    # path('comments/', include('apps.comments.api.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.products.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('apps.reviews.urls')),
    path('', include('apps.basket.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('apps.tags.urls')),
    path('', include('apps.trainer.urls')),
    path('', include('apps.schedules.urls')),
    path('', include('apps.courses.urls')),
    path('', CourseListView.as_view(), name='home'),
    path('', include('apps.buy.urls')),

]


urlpatterns += api_urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
