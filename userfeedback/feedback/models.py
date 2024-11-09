from django.db import models

class UserFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"
