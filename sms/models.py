from django.db import models

# Create your models here.

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)

class Messages(models.Model):
    phone_number = models.ForeignKey(PhoneNumber,related_name="messages",on_delete=models.CASCADE)
    send_at = models.DateField()
    from_target = models.BooleanField(default=True)
    content = models.TextField(default="")