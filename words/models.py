from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
class DayNumber(models.Model):
    title = models.CharField(_("Nomi"), max_length=50, null=False, blank=False)
    view_home = models.BooleanField(_("Faollik"), default=False)
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Yangilangan vaqt"), auto_now=True)

    class Meta:
        verbose_name = 'Kun nomi'
        verbose_name_plural = 'Kun'
        ordering = ('created_at', 'updated_at')

    def __str__(self):
        return self.title

