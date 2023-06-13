from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from mysite.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls', namespace='mysite')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]