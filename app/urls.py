# -*- coding: utf-8 -*-

from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
# from theme import views
import os, sys
sys.path.append(os.getcwd())


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # url(r'^api/activity', include('activity.urls')),
    path('api', include(router.urls)),
    # path('api/activity', activity_api),
    # path('api/type-activity', type_activity_api),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('', views.home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# path('books_cbv/', include('books_cbv.urls', namespace='books_cbv')),
# path('books_fbv/', include('books_fbv.urls', namespace='books_fbv')),
# path('books_fbv_user/', include('books_fbv_user.urls', namespace='books_fbv_user')),
