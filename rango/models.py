from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# model for database
class Category(models.Model):
    #PK
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.name) 
        super(Category, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name_plural ='Categories'
        
    def __str__(self):
        return self.name

#model page
class Page(models.Model): 
    # FK one to many relationship
    category = models.ForeignKey(Category) 
    title = models.CharField(max_length=128) 
    url = models.URLField()
    views = models.IntegerField(default = 0)   


# for debugging, string representation of the object (toString) 
    def __str__(self):  
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    website = models.URLField(blank=True) 
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self): 
        return self.user.username

