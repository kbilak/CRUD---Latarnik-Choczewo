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
        verbose_name = 'Język'
        verbose_name_plural = 'Języki'


class Code(models.Model):
    code = models.CharField(max_length=1024, default='')

    def __str__(self):
        return '%s' %(self.code)
    
    class Meta:
        ordering = ('code',)
        verbose_name = 'Kod'
        verbose_name_plural = 'Kody'


class Translation(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=None)
    code = models.ForeignKey(Code, on_delete=models.CASCADE, default=None)
    translation = models.CharField(max_length=1024, default='', blank=True, null=True)

    def __str__(self):
        return '%s' %(self.translation)
    
    class Meta:
        ordering = ('code', 'language', )
        verbose_name = 'Tłumaczenie'
        verbose_name_plural = 'Tłumaczenia'
