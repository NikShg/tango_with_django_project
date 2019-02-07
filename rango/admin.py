from django.contrib import admin

from rango.models import Category, Page
from polls.models import Choice,Question


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
# register in admin panel
admin.site.register(Category) 
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
