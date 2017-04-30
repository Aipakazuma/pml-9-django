from django.db import models


class Review(models.Model):
    review_text = models.TextField()
    sentiment = models.IntegerField()
    created = models.DateTimeField()
