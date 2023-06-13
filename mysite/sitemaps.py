from django.contrib.sitemaps import Sitemap

from .models import Post


def lastmod(obj):
    return obj.updated


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()
