from django.contrib import admin

from apps.blog.models import Category, Author


class CategoryAdmin(admin.ModelAdmin):
    '''
         custom Admin panel
    '''
    # add search bar
    search_fields = ['name']

    # indicates the attributes to display in the admin panel
    list_display = ('name', 'status', 'create_at')


class AuthorAdmin(admin.ModelAdmin):
    '''
        Custom Admin panel
    '''
    # add search bar
    search_fields = ['name', 'lastName', 'email']
    
    #indicates the attributes to display in the admin panel
    list_display = ('name','lastName', 'gmail', 'status', 'create_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
