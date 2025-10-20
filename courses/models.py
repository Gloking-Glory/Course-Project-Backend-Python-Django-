from django.db import models
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    course_title = models.CharField(max_length=255, db_index=True)
    university = models.CharField(max_length=255, db_index=True)
    duration = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    fees = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at'])]

    def __str__(self):
        return f"{self.course_title} - {self.university}"
