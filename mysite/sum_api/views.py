from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'sum_api/home.html', {'name': 'There'})

def add(request):


	val1 = None
	val2 = None
	res = 'enter proper value'

	try:
		val1 = int(request.GET['num1'])
		val2 = int(request.GET['num2'])
		res = val1 + val2

	except ValueError:
		print("Please enter integer value")

	
	return render(request, "sum_api/result.html", {'result': res})

	