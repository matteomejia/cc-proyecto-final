from django.db import models
from django.utils.translation import gettext_lazy as _

from cloud.workshops.models import Workshop
from cloud.users.models import User, Student
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))

    paid = models.BooleanField(_('paid'), default=False)
    paid_at = models.DateTimeField(_('paid at'), blank=True, null=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.user.email

    def get_inscription_count(self):
        return self.inscriptions.count()

    def get_total(self):
        total = 0
        for inscription in self.inscriptions.all():
            total += inscription.get_final_price()
        return total

class Inscription(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('order'), related_name='inscriptions', blank=True, null=True)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, verbose_name=_('inscription'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('student'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))


    paid = models.BooleanField(_('paid'), default=False)
    paid_at = models.DateTimeField(_('paid at'), blank=True, null=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + " - " + self.workshop.title

    class Meta:
        verbose_name = _('inscription')
        verbose_name_plural = _('inscription')


    def get_item_price(self):
        return self.workshop.price

    def get_item_discount_price(self):
        return self.workshop.discount_price

    def get_amount_saved(self):
        return self.get_item_price() - self.get_item_discount_price()

    def get_final_price(self):
        if self.workshop.discount_price:
            return self.get_item_discount_price()
        return self.get_item_price()


