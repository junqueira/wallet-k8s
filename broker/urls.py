from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            # Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^api/', include('broker.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        url(r'^(?P<path>favicon\..*)$', serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 'django.contrib.staticfiles.views.serve', dict(insecure=True)),
    )

# urlpatterns = format_suffix_patterns(urlpatterns)
