from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from datetime import datetime

# POSTS
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Slug',unique=True, max_length=255)
    seo_keywords = models.CharField('SEO Keywords', max_length=255, blank=True, null=True)
    seo_description = models.CharField('SEO Description', max_length=255, blank=True, null=True)
    is_published = models.BooleanField('Published', default=True)
    pub_date = models.DateTimeField('Date Published', default=datetime.now)

    class Meta:
        ordering = ['-pub_date']
        verbose_name='Blog Post'
        verbose_name_plural='All Posts'

    def __str__(self):
        return "%s" % self.title
