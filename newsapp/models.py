from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
# class Tags(models.Model):
#     tags=models.CharField(max_length=255)\
    
#     class Meta:
#         verbose_name='Tag'
#         verbose_name_plural='Tags'

#     def __str__(self) -> str:
#         return self.tags

class News(models.Model):
    title = models.CharField("Title", max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank = True, null=True)
    tegs  = TaggableManager()
    date_creation = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self) -> str:
        return self.title

