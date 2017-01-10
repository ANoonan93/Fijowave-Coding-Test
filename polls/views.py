from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.core import serializers
from .models import Machines


# Create your views here.
def home(request):
	return render(request, 'home.html')

def pieChart(request):
	return render(request, 'Pie_Chart.html', {'firmwareobject': Machines.objects.all()})

def j_display(request, pretty=False):
	leads_as_json = serializers.serialize('json', Machines.objects.all())
	if pretty:
		leads_as_json = json.dumps(json.loads(leads_as_json), indent=2)  
	return HttpResponse(leads_as_json, content_type='json')