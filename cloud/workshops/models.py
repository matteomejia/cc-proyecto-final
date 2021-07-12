from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import LEVEL_CHOICES, STATUS_CHOICES

# Create your models here.
class Topic(models.Model):
    name = models.CharField(_(), max_length=254)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='topics', blank=True, null=True)

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

    start_date = models.DateField(_('start date'))
    hours = models.PositiveSmallIntegerField(blank=True, null=True)
    weeks = models.PositiveSmallIntegerField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)

    level = models.PositiveSmallIntegerField(_('level'), choices=LEVEL_CHOICES, default=1)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')