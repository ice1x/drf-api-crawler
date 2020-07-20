from django.db import models


class Posts(models.Model):
    """
    Ycombinator posts
    """
    # id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    created = models.DateTimeField()
