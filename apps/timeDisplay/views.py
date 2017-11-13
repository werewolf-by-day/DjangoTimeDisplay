from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
 	context = {
  	"time": strftime("%b %d, %Y %I:%M %p", localtime()) 
  	}
 	return render(request,'timeDisplay/index.html', context)

