from django.db import models

class AnnounType(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Announ(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    file = models.FileField(upload_to = "others/", null=True, blank=True)
    type_of = models.ForeignKey(AnnounType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

