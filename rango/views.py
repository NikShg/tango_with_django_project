from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
#from unicodedata import category
#def index(request): 
#    return HttpResponse("Rango says hey there partner!<br/> <a href='/rango/about/'>About</a>.")

def about (request):
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>. ")
    context_dict ={'boldmessage': "This tutorial has been put together by 2207113"}
    return render(request, 'rango/about.html', context = context_dict)

def index(request):
     # Construct a dictionary to pass to the template engine as its context. 
     # Note the key boldmessage is the same as {{ boldmessage }} in the template! 
     #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
     # Return a rendered response to send to the client.
     # We make use of the shortcut function to make our lives easier.
     # Note that the first parameter is the template we wish to use. 
     #return render(request,'rango/index.html', context=context_dict)
     
     #get top 5 categories from database by likes, place in context_dict
     
    category_list = Category.objects.order_by('-likes')[:5] 
    page_list = Page.objects.order_by('-views')[:5]
    
    context_dict = {'categories': category_list, 'pages': page_list}
     
     #render the response
    return render(request, 'rango/index.html', context_dict)
 
 # defin context dict, extract data from models, add data to dict
def show_category(request, category_name_slug):
    #dict to pas to template
    context_dict={}
    try:
        #find category slug => gets instace or raises an exception
        category = Category.objects.get(slug = category_name_slug)
         
        # get associated pages
        pages = Page.objects.filter(category=category)
         
        #add tp the template under name pages
        context_dict['pages'] = pages
         
        # add cat to verify whtether cat exists
        context_dict['category'] = category;
    except Category.DoesNotExist:
        # if there is no
        context_dict['category']= None
        context_dict['pages']=None
        # render and return
        
    return render (request,'rango/category.html',context_dict)

def add_category(request):
    
    form = CategoryForm()
    #A HTTP Post
 
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        # check validity
        if form.is_valid():
            #save cat to db
            form.save(commit = True)
            
            # save direct to index page
            return index(request)
        else:
            #if error
            print(form.errors)
            
            #render
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        category = None
        
    form = PageForm()
    if request.method =='POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'category': category}
    return render(request,'rango/add_page.html', context_dict)
    