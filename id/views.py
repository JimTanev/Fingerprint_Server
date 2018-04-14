from django.template import loader
from django.http import HttpResponse
from .models import Person


def index(request, person_id):
    try:
        person = Person.objects.get(iden_num=person_id)
    except Person.DoesNotExist:
        template = loader.get_template('404.html')
        context = {'person_id': person_id}
        return HttpResponse(template.render(context, request))
    template = loader.get_template('index.html')
    context = {'person': person}
    return HttpResponse(template.render(context, request))

