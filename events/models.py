from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    start_time = models.DateTimeField(auto_now_add=False, null=False)
    end_time = models.DateTimeField(auto_now_add=False, null=False)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    public = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Guest(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=False, null=False)
    attending = models.BooleanField(default=False)
    event = models.ForeignKey(Event, related_name='guests', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def guests_list(cls):
        return cls.objects.distinct('email')

    class Meta:
        ordering = ['-email', '-created_date']

    def __str__(self):
        if self.name:
            return f"{self.name} <{self.email}>"
        return f"{self.email}"
