from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.blog.models import Category, Author, Post

class CategoryResource(resources.ModelResource):
    '''
        allow export and import data from admin panel
    '''
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    '''
         custom Admin panel
    '''
    # add search bar
    search_fields = ['name']

    # indicates the attributes to display in the admin panel
    list_display = ('name', 'status', 'create_at')

    # Display a button witch allows you to export and import data
    resource_class = CategoryResource

class AuthorResource(resources.ModelResource):
    '''
        allow export and import data from admin panel
    '''
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    '''
        Custom Admin panel
    '''
    # add search bar
    search_fields = ['name', 'lastName', 'email']
    
    #indicates the attributes to display in the admin panel
    list_display = ('name','lastName', 'gmail', 'status', 'create_at',)

    # Display a button witch allows you to export and import data
    resource_class = AuthorResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
