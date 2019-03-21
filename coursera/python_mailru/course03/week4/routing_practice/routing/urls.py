from django.conf.urls import url
import routing.views as routing

urlpatterns = [
    url(r'^simple_route/$', routing.simple_route),
    url(r'^slug_route/(?P<pk>[0-9a-z-_]{1,16})/$', routing.slug_route),
    url(r'^sum_route/(?P<a>\d+)/(?P<b>\d+)/$', routing.sum_route),
    url(r'^sum_get_method/$', routing.sum_get_method),
    url(r'^sum_post_method/$', routing.sum_post_method),
]
