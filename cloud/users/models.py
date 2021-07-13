from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from django_extensions.db.fields import AutoSlugField

from .managers import UserManager
from .choices import ROLE_CHOICES


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # Mandatory Data
    email = models.EmailField(_("email address"), max_length=254, unique=True)
    first_name = models.CharField(
        _("first name"), max_length=100, null=True, blank=True
    )
    last_name = models.CharField(_("last name"), max_length=100, null=True, blank=True)
    country = CountryField(default="PE", verbose_name=_("country"))

    role = models.PositiveSmallIntegerField(_("role"), choices=ROLE_CHOICES, default=1)
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    phone = models.CharField(_("phone"), max_length=100, blank=True, null=True)
    school = models.CharField(_('school'), max_length=254, blank=True, null=True)
    document = models.CharField(_("document"), max_length=100, blank=True, null=True)

    # Permissions
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)

    # Tracking
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    slug = AutoSlugField(populate_from=['first_name', 'last_name'], unique=True)
    
    first_name = models.CharField(_('first_name'), max_length=254)
    last_name = models.CharField(_('last name'), max_length=254)
    date_of_birth = models.DateField(_('date of birth'))
    school = models.CharField(_('school'), max_length=254)

    parent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('parent'))

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("users:student-edit", kwargs={
            'pk': self.pk
        })