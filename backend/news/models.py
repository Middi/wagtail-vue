from django.db import models

from wagtail.api import APIField

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField

# Create your models here.

class NewsPage(Page):
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    ) 
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-300x300', source='image')),
    ]