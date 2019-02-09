import os  
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'tango_with_django_project.settings') 
import django
django.setup()
from rango.models import Category,Page

def populate():
    #dictionaries
    python_pages=[  {"title": "Official Python Tutorial", 
                     "url":"http://docs.python.org/2/tutorial/", "views":20}, 
                      {"title":"How to Think like a Computer Scientist", 
                       "url":"http://www.greenteapress.com/thinkpython/" ,"views":35}, 
                      {"title":"Learn Python in 10 Minutes", 
                       "url":"http://www.korokithakis.net/tutorials/python/", "views":15}]
    django_pages = [ {"title":"Official Django Tutorial", 
                      "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views":20},
                       {"title":"Django Rocks", 
                        "url":"http://www.djangorocks.com/", "views":35}, 
                       {"title":"How to Tango with Django",
                        "url":"http://www.tangowithdjango.com/", "views":15}]
    other_pages = [ {"title":"Bottle", 
                     "url":"http://bottlepy.org/docs/dev/","views":20}, 
                     {"title":"Flask", 
                      "url":"http://flask.pocoo.org", "views":35} ]
    cats = {"Python": {"pages": python_pages,"views":128,"likes":64}, 
            "Django": {"pages": django_pages,"views":64,"likes":32}, 
            "Other Frameworks": {"pages": other_pages,"views":32,"likes":16}
            
            }
    
    #add_cat("Django", views=64, likes =32)
    # add_cat("Other Frameworks", views = 32,likes =16)
            
    #more categories go to these dictionaries
    
    #next, goes through cats dictionary, adds catgories and adds pages for that category
    
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"]) 
        for p in cat_data["pages"]:
            add_page(c,p["title"], p["url"],p["views"])
            
            
            
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0} - {1}".format(str(c), str(p)))
            
def add_page(cat,title,url, views):
    #check whether the entry exists
    p=Page.objects.get_or_create(category =cat, title=title)[0]
    p.url=url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):
    c=Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
#   c=Category.objects.get_or_create(views=views)[0]
#   c=Category.objects.get_or_create(likes=likes)[0]
    c.save()
    return c

if __name__=='__main__':
    print("Starting Rango population script ...")
    populate()

        