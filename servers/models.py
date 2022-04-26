from django.db import models


class Servers(models.Model):
    server_name = models.CharField(max_length=100)
    url = models.URLField(max_length=25)
    port = models.IntegerField()
    password = models.CharField(max_length=100)
    image = models.URLField()
    alt_image = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.server_name
