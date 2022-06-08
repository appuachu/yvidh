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


class depevents(models.Model):
    def __str__(self):
        return self.dep_event_name
    dep_image_event=models.ImageField(upload_to='static')
    dep_date_event=models.IntegerField()
    dep_month_event=models.TextField()
    dep_event_name=models.TextField()
    dep_event_head=models.TextField()
    dep_event_detail=models.TextField()
    dep_description_event=models.TextField()
    dep_event_coordinator=models.TextField(max_length=10)
    dep_register_link=models.TextField()
    dep_registration_prize=models.TextField()
    dep_prize_pool=models.TextField()
    dep_first_prize=models.TextField()
    dep_second_prize=models.TextField()
    dep_rule1=models.TextField()
    dep_rule2=models.TextField()
    dep_rule3=models.TextField()
    dep_rule4=models.TextField()
    dep_rule5=models.TextField()
    dep_rule6=models.TextField()
    dep_rule7=models.TextField()

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
