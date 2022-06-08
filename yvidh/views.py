from django.shortcuts import render
from . models import *
from django.views.generic.detail import DetailView
from django.db.models import Q
# Create your views here.
def home(request):
    event=events.objects.all()
    gale=gallery.objects.all()
    show=shows.objects.all()
    depevent=depevents.objects.all()

    return render(request,"index.html",{'event':event,'gale':gale,'show':show,'depevent':depevent})


class eventdetails(DetailView):
    model = events
    template_name = 'event.html'
    context_object_name = 'l'

class depeventdetails(DetailView):
    model = depevents
    template_name = 'depevent.html'
    context_object_name = 'x'

def searching(request):
    event=None
    gale=None
    query=None


    if 'q' in request.GET:
        query=request.GET.get('q')
        gale=gallery.objects.all().filter(Q(caption_gallery__contains=query))
        # show=shows.objects.all().filter(Q(description_show__contains=query)|Q(show_name__contains=query)|Q(time_show__contains=query))
        event=events.objects.all().filter(Q(event_name__contains=query)|Q(description_event__contains=query))
    return render(request,"search.html",{'qr':query,'event':event,'gale':gale})


