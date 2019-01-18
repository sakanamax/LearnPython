from django.shortcuts import render, redirect
from django.http import HttpResponse
from ugo import models
from datetime import datetime
# Create your views here.

def index(request):
	now = datetime.now()
	return render(request, "index.html", locals())

def listall(request):
	all = models.urlist.objects.all()
	now = datetime.now
	return render(request, "listall.html", locals())

def notfound(request, item):
	now = datetime.now
	return render(request, 'notfound.html', {'id':item, 'now': now})

def gourl(request, target):
	try:
		rec = models.urlist.objects.get(short_url = target)
		target_url = rec.src_url
		rec.count = rec.count + 1
		rec.save()
	except:
		target_url = '/notfound/' + target
	return redirect(target_url) 
