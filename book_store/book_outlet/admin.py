from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = ({"slug": ("title",)})
    list_filter = ("rating", "author",)
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)