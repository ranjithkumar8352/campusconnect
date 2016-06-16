from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.
@csrf_exempt
def hello(request):
	print request.body
	template = loader.get_template("test.html")
	return HttpResponse(template.render())
