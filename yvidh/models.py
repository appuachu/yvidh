from django.db import models

# Create your models here.
class events(models.Model):
    def __str__(self):
        return self.event_name
    image_event=models.ImageField(upload_to='static')
    date_event=models.IntegerField()
    month_event=models.TextField()
    event_name=models.TextField()
    event_head=models.TextField()
    event_detail=models.TextField()
    description_event=models.TextField()
    event_coordinator=models.TextField(max_length=10)
    register_link=models.TextField()
    registration_prize=models.TextField()
    prize_pool=models.TextField()
    first_prize=models.TextField()
    second_prize=models.TextField()
    rule1=models.TextField()
    rule2=models.TextField()
    rule3=models.TextField()
    rule4=models.TextField()
    rule5=models.TextField()
    rule6=models.TextField()
    rule7=models.TextField()




class gallery(models.Model):
    image_gallery=models.ImageField(upload_to='static')
    caption_gallery=models.TextField()

class shows(models.Model):
    def __str__(self):
        return self.show_name
    image_show=models.ImageField(upload_to='static')
    show_name=models.TextField()
    show_price=models.IntegerField()
    time_show=models.IntegerField()
    description_show=models.TextField()
