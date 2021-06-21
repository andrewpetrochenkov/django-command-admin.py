from django.db import models

class Command(models.Model):
    name = models.TextField(primary_key=True)
    app = models.TextField()

    class Meta:
        db_table = 'django_command_admin_command'
        indexes = [
           models.Index(fields=['name',]),
           models.Index(fields=['app',]),
        ]
        ordering = ('name',)
        unique_together = (('app','name'),)
