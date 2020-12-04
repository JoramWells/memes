from django.db import models

CATEGORY_CHOICES = (
    ('A', 'Agriculture'),
    ('B', 'Banking'),
    ('E', 'Electrical'),
    ('EC','Economics'),
    ('M', 'Mechanic'),
    ('S', 'Science'),
    ('GS', 'Geo-Science'),

)


class PostQ(models.Model):
    content=models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

class Post(models.Model):
    keyword = models.CharField(max_length=255,blank=True, null=True)
    min_videos = models.IntegerField(blank=True, null=True)    
    created_on=models.DateTimeField(auto_now_add=True, blank=True, null=True)

    
    def __str__(self):
        return self.title