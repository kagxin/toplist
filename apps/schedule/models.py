from django.db import models
from django.utils.timezone import now


class Entry(models.Model):
    site_choices = (
        (1, '糗事百科'),
        (2, '知乎')
    )

    target = models.IntegerField('站点类型', choices=site_choices, default=1)
    title = models.CharField(max_length=256, default='')
    content = models.TextField(default='')
    rank = models.IntegerField(default=0)
    url = models.CharField(max_length=256, default='')
    release_date = models.DateTimeField(default=now, db_index=True)

    class Meta:
        db_table = 'entry'
        unique_together = ("target", "rank")
        ordering = ['target', 'rank', '-release_date']

