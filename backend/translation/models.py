from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30, default='')
    code = models.CharField(max_length=2, default='')
    active = models.BooleanField(default=True)
    number = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return '%s' %(self.name)
    
    class Meta:
        ordering = ('number',)
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Code(models.Model):
    code = models.CharField(max_length=1024, default='')

    def __str__(self):
        return '%s' %(self.code)
    
    class Meta:
        ordering = ('code',)
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'


class Translation(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=None)
    code = models.ForeignKey(Code, on_delete=models.CASCADE, default=None)
    translation = models.CharField(max_length=1024, default='', blank=True, null=True)

    def __str__(self):
        return '%s' %(self.translation)
    
    class Meta:
        ordering = ('code', 'language', )
        verbose_name = 'Translation'
        verbose_name_plural = 'Translations'
