from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# admin.site.register(Author)
# Define the admin class


# Register the admin class with the associated model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


class BookInstanceInline(admin.TabularInline):
    model = BookInstance  # 使用 BookInstance 模型
    extra = 0  # 指定預設顯示的空白行數


admin.site.register(Author, AuthorAdmin)

# admin.site.register(Book)
# admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')  # 確保使用的字段正確
    inlines = [BookInstanceInline]
# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
