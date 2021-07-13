from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from .choices import LEVEL_CHOICES, STATUS_CHOICES

# Create your models here.
class Topic(models.Model):
    name = models.CharField(_('name'), max_length=254)
    description = models.TextField(_('description'), blank=True, null=True)
    logo = models.ImageField(_('logo'), upload_to='topics', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('topic')
        verbose_name_plural = _('topics')


class Workshop(models.Model):
    slug = models.SlugField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=_('topic'))

    title = models.CharField(_('title'), max_length=254)
    description = models.TextField(_('description'))

    price = models.FloatField(_('price'))
    discount_price = models.FloatField(_('discount price'), blank=True, null=True)

    image = models.ImageField(_('image'), upload_to='workshops')

    min_age = models.PositiveSmallIntegerField(blank=True, null=True)
    max_age = models.PositiveSmallIntegerField(blank=True, null=True)

    start_date = models.DateField(_('start date'))
    hours = models.PositiveSmallIntegerField(blank=True, null=True)
    weeks = models.PositiveSmallIntegerField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)

    level = models.PositiveSmallIntegerField(_('level'), choices=LEVEL_CHOICES, default=1)
    active = models.BooleanField(_('active'), default=True)
    private = models.BooleanField(_('private'), default=False)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("workshops:workshop-detail", kwargs={
            'slug': self.slug
        })
        
    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')