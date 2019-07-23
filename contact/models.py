from django.db import models


class ContactMessage(models.Model):
    subject = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False)
    text = models.TextField(null=False, blank=False, verbose_name='Message')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message <from:{self.email}>"
