from django.db import models

class Feed(models.Model):
    url = models.URLField()
    title = models.CharField(max_length = 200)
    isActive = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title
        
class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length = 200)
    publicationDate = models.DateTimeField()
    description = models.TextField()
    url = models.URLField()
    
    def __str__(self):
        return self.title
    
    