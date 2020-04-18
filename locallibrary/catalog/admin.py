from django.contrib import admin
from .models import Author, Book, Genre, BookInstance, Language

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)

# Inline class for Book(to later show in the Author section)
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Register the admin class for Author with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the admin classes for BookInstance with the associated model using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            "fields": (
                'book',
                'imprint',
                'id'
            ),
        }),
        ('Availability', {
            "fields": (
                'status',
                'due_back'
            )
        }),
    )
    
# Inline class for BookInstance(to later show in the Book section)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

