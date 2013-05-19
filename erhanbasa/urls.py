from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from blog.views import articles, article, loop, categories, contact
from blog.models import Category, Post
from django.contrib import admin
from erhanbasa import settings
admin.autodiscover()
handler404 = 'blog.views.articles'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'erhanbasa.views.home', name='home'),
    # url(r'^erhanbasa/', include('erhanbasa.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', articles),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^about/$', direct_to_template, {'template':'about.html'}),
    url(r'^contact/$', contact),
    url(r'^blog/$', loop),
    url(r'^blog/(?P<slug>[\w-]+)/$', article),
    url(r'^(?P<slug>[\w-]+)/$', categories),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)