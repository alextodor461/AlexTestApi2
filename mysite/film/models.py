from django.db import models
from datetime import date
from django.contrib.auth.models import User


class IntegerRangeField(models.IntegerField):

    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Film(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    rate = IntegerRangeField(min_value=0, max_value=5, default=0, blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, default = None)


class Comments(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, default = None)
