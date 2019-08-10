from django.contrib import admin
from .models import Entry
# Register your models here.
from django.contrib import admin


# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('target', 'rank', 'title', 'content', 'url', 'release_date')
#     # search_fields =


admin.site.register(Entry, EntryAdmin)