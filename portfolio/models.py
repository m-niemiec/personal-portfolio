from django.db import models


# Model for portfolio project entry.
class Project(models.Model):
    title = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to="portfolio/images/")
    description = models.TextField(max_length=1000)
    details = models.TextField(max_length=10000, blank=True)
    screenshot_main = models.ImageField(upload_to="portfolio/images/", blank=True)
    screenshot_1 = models.ImageField(upload_to="portfolio/images/", blank=True, null=True)
    screenshot_2 = models.ImageField(upload_to="portfolio/images/", blank=True, null=True)
    screenshot_3 = models.ImageField(upload_to="portfolio/images/", blank=True, null=True)
    created = models.DateTimeField(blank=True)
    url_github = models.URLField(blank=True)
    url_live = models.URLField(blank=True)

    def __str__(self):
        return self.title