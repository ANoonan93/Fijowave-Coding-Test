from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.core import serializers
from .models import Machines


# Create your views here.
def home(request):
	return render(request, 'home.html')

def pieChart(request):
	data = Machines.objects.all()
	return render(request, 'Pie_Chart.html', {'firmwareobject': data})

def j_display(request, pretty=False):
	leads_as_json = serializers.serialize('json', Machines.objects.all())
	if pretty:
		leads_as_json = json.dumps(json.loads(leads_as_json), indent=2)  
	return render(request, "j_display.html", {'data': leads_as_json})