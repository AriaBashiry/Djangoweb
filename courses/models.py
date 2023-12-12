from django.db import models

# Create your models here.
class Topic(models.Model):
    Title = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)

class Episode(models.Model):
    TopicID = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    Image = models.ImageField()
