from django.contrib import admin

from django.contrib import admin

# Register your models here.
from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Snippet, SnippetAdmin)