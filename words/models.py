from django.db import models
from django.utils import timezone
class DayNumber(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    view_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at', 'updated_at')

    def __str__(self):
        return self.title

