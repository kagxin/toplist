from django.db import models

# Create your models here.

from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-id']


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    contents = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-id']
