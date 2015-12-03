from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = 'locations'
    def get_absolute_url(self):
        return "reports/%s" % self.name_slug
    def __unicode__(self):
        return self.name

class Tickets(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    county = models.ForeignKey(Location)
    site_id = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name
