from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = 'locations'
    def get_absolute_url(self):
        return "locations/%s" % self.name_slug
    def __unicode__(self):
        return self.name

class Violation(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = 'violations'
    def get_absolute_url(self):
        return "violations/%s" % self.name_slug
    def __unicode__(self):
        return self.name

class License(models.Model):
    plate = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "reports/%i" % self.id
    def __unicode__(self):
        return self.plate

class Tickets(models.Model):
    ticket_number = models.CharField(max_length=50)
    ticket_date = models.DateTimeField()
    violation = models.ForeignKey(Violation)
    location = models.ForeignKey(Location)
    plate = models.ForeignKey(License)
    def __unicode__(self):
        return self.ticket_number
