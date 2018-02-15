from django.db import models
from django.utils import timezone

#the model's name is post and it's properties are title, text, created_date, published_date, and author.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) #automatically marks the author as the signed in user
    title = models.CharField(max_length=200) #the title can't be any more than 200 characters long
    text = models.TextField() #TextField is unlimited text
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
