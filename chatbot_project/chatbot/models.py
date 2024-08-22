from django.db import models

# Create your models here.

class ChatLog(models.Model):
    user_query = models.CharField(max_length=255)
    bot_response = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_query
