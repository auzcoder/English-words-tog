from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from users.models import CustomUsers

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

class WordLevel(models.Model):
    title = models.CharField(_("Nomi"), max_length=50, null=False, blank=False)
    view_home = models.BooleanField(_("Faollik"), default=False)
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Yangilangan vaqt"), auto_now=True)

    class Meta:
        verbose_name = 'So\'zning qiyinlik darajasi'
        verbose_name_plural = 'So\'zning qiyinlik darajasi'
        ordering = ('-created_at', 'updated_at')

    def __str__(self):
        return self.title


class Words(models.Model):
    user = models.ForeignKey(CustomUsers, on_delete=models.SET_DEFAULT, default=1)
    day = models.ForeignKey(DayNumber, on_delete=models.SET_NULL, null=True, blank=True)

    word = models.CharField(_("Spelling - Aytilishi"), max_length=200, null=False, blank=False)
    transcription = models.CharField(_("Pronunciation - O'qilishi"), max_length=200, null=True, blank=True)
    translation = models.CharField(_("Translation - Tarjimasi"), max_length=300, null=False, blank=False)

    image = models.ImageField(_("Rasm"), upload_to='Words/%Y/%m', blank=True, null=True)

    level = models.ForeignKey(WordLevel, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Yangilangan vaqt"), auto_now=True)

    def get_full_word(self):
        full_word = self.word + ' - ' + self.translation
        return full_word

    class Meta:
        verbose_name = 'So\'zlar'
        verbose_name_plural = 'So\'zlar'

    def __str__(self):
        return self.get_full_word()

