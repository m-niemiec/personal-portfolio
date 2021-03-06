from django.db import models


# Model for secondary category - defines if entry is "Note" or Code Snippet".
class SubCategory(models.Model):
    sub_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.sub_category


# Model for main category - defines language.
class Category(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.category


# One model for notes and code snippets.
class Note(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    details = models.TextField(max_length=10000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
