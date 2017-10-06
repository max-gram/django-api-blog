from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from redactor.fields import RedactorField
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from api_django_blog.extra import ContentTypeRestrictedFileField

# POSTS
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Slug',unique=True, max_length=255)
    seo_keywords = models.CharField('SEO Keywords', max_length=255, blank=True, null=True)
    seo_description = models.CharField('SEO Description', max_length=255, blank=True, null=True)
    thumbnail = ContentTypeRestrictedFileField( #'Cover Image',
        help_text='JPEG, JPG, PNG, GIF - 10 Mb Max',
        upload_to='posts/thumbs',
        content_types=['image/jpeg', 'image/jpg', 'image/png', 'image/gif'],
        max_upload_size=10485760, 
        null=True
    )
    thumb = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFit(1000, 1000)],
        # format='JPEG',
        options={'quality': 80}
    )
    body = RedactorField(
        verbose_name=u'Post Text',
        allow_file_upload=False,
        allow_image_upload=True,
        max_length=5000,
        blank=True,
        null=True
    )
    is_published = models.BooleanField('Published', default=True)
    pub_date = models.DateTimeField('Date Published', default=datetime.now)

    class Meta:
        ordering = ['-pub_date']
        verbose_name='Blog Post'
        verbose_name_plural='All Posts'

    def __str__(self):
        return "%s" % self.title
