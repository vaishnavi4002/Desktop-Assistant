

from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_text


