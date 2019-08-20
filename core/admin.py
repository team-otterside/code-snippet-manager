from django.contrib import admin
from core.models import Snippet

# Models registered for Code Snippet 

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass