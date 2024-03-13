from django.db import models

class SampleDB(models.Model):
    sample1 = models.IntegerField('sample1', null=True, blank=True)
    sample2 = models.CharField('sample2', max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = 'sample_table'
        verbose_name_plural = 'sample_table'