from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField("Job Description", max_length=500)
    pay_rate = models.CharField("Pay Rate", max_length=500)
    is_visible = models.BooleanField(default = False)
    dateMade = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

