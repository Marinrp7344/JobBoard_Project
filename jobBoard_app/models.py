from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])


class Post(models.Model):
    TOOLS = (
        ('Lawn Mower','LAWN MOWER'),
        ('shovel', 'SHOVEL'),
        ('Rake', 'RAKE')
    )
    title = models.CharField(max_length=200)
    body = models.CharField("About", max_length=200)
    description = models.TextField("Job Description", max_length=200, blank = True)
    tools = models.CharField(max_length=200, choices=TOOLS, blank = True)
    pay_rate = models.CharField("Pay Rate", max_length=500)
    is_visible = models.BooleanField(default = False)
    dateMade = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete = models.CASCADE,null=True)
   
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
   
    class Meta:
        permissions = [("can_access", "Is able to access the Post")]
