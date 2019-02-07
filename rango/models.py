from django.db import models

# model for database
class Category(models.Model):
    #PK
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
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

 
# for debugging, string representation of the object (toString) 
    def __str__(self):  
        return self.title