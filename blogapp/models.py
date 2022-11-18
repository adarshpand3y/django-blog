from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title