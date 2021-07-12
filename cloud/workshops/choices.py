from django.utils.translation import gettext_lazy as _

LEVEL_CHOICES = [
    (1, _('beginner')),
    (2, _('intermediate')),
    (3, _('advanced'))
]

STATUS_CHOICES = [
    (1, _('public')),
    (2, _('private')),
    (3, _('inactive'))
]