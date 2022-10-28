from email.policy import default
from django.db import models


class Category(models.Model):

    id = models.AutoField(primary_key=True)

    # indicates the category to which the blog belong
    name = models.CharField(
        'Category Name', max_length=100, null=True, blank=True)

    # indicates if the status of the category is active or not
    status = models.BooleanField('Status On|Off', default=True)

    # indicates the creation category of the date
    create_at = models.DateField(
        'Creation date', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(models.Model):

    id = models.AutoField(primary_key=True)

    # indicates the Author's name
    name = models.CharField(
        "Author's Name", max_length=255, null=False, blank=False)

    # indicates the Author's last name
    lastName = models.CharField(
        "Author's Last Name", max_length=255, null=False, blank=False)

    # indicates te Author's facebook
    facebook = models.URLField(
        'Facebook', max_length=100, null=True, blank=True)

    # indicates te Author's twitter
    twitter = models.URLField(
        'Twitter', max_length=100, null=True, blank=True)

    # indicates the Author's instagram
    instagram = models.URLField(
        'Instagram', max_length=100, null=True, blank=True)

    # indicates the Author's email
    gmail = models.EmailField('Gmail', null=False, blank=False, max_length=60)

    #  indicates if the status of the author is active or not
    status = models.BooleanField('Author On|Off', default=True)

    # indicates the creation of the author
    create_at = models.DateField(
        'Creation date', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.lastName}, {self.name}"
        
