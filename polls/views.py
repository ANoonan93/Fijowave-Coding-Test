from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def pieChart(request):
	return render(request, 'Pie_Chart.html')

def j_display(request):
	return render(request, 'j_display.html')