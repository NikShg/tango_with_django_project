from django.contrib import admin

from rango.models import Category, Page
from polls.models import Choice,Question
from rango.models import UserProfile

admin.site.register(UserProfile)
# to include head
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# customise admin to populate slug field
class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug':('name',)}

# register in admin panel
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Page, PageAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)
