from django.db import models

class Call(models.Model):
    app = models.TextField()
    name = models.TextField()
    args = models.TextField(null=True)
    stdout = models.TextField(null=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        db_table = 'django_command_admin_call'
        indexes = [
           models.Index(fields=['name',]),
        ]
