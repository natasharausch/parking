import os, sys, string, csv, datetime, time, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parking.settings")

from django.conf import settings

from myapp.models import Violation, Location, License, Tickets 

from django.template.defaultfilters import slugify, urlize

django.setup()

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

reader = csv.reader(open("citations.csv", "rU"), dialect='piper')

for row in reader:
    citno = row[0]
    dt = time.strptime(row[1], "%Y-%m-%d %H:%M")
    viodate = datetime.datetime(dt.tm_year, dt.tm_mon, dt.tm_mday, dt.tm_hour, dt.tm_min)
    vio, viocreated = Violation.objects.get_or_create(name=row[2], name_slug=slugify(row[2]))
    loc, loccreated = Location.objects.get_or_create(name=row[3], name_slug=slugify(row[3]))
    lic, liccreated = License.objects.get_or_create(plate=row[4])
    tic, ticcreated = Tickets.objects.get_or_create(ticket_number=citno, ticket_date=viodate, violation=vio, location=loc, plate=lic)
    print tic
