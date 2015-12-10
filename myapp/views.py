from django.shortcuts import render
from django.db.models import Count

from .models import Location, Tickets, Violation

def homePage(request):
    locations = Location.objects.annotate(Count('tickets')).order_by('-tickets__count')[:25]
    violations = Violation.objects.order_by('name').annotate(Count('tickets')).order_by('-tickets__count')
    return render(request, 'reports/index.html', {'locations': locations, 'violations': violations})

def locationdetail(request, location_slug):
    location = Location.objects.get(name_slug=location_slug)
    total = Tickets.objects.filter(location=location).count()
    tickets = Tickets.objects.filter(location=location).values('violation__name').annotate(Count('id')).order_by('-id__count')
    return render(request, 'reports/location.html', {'location': location, 'tickets':tickets, 'total': total})

def violationdetail(request, violation_slug):
    violation = Violation.objects.get(name_slug=violation_slug)
    tickets = Tickets.objects.filter(violation=violation)
    return render(request, 'reports/violation.html', {'violation': violation, 'tickets':tickets})
