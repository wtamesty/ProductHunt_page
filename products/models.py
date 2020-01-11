from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    body = models.TextField()
    pub_date = models.DateTimeField(default=now, editable=False)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body_text[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
