from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader
from anagramsapp.forms import First
from django.views.generic.edit import FormView


# Create your views here.

def index(request):
	f=open('source.txt',"r")
	content=f.readlines()
	print(content)
	context={'content': content}
	
	# template = loader.get_template('index.html')
	return render(request, 'home.html', context)

	# return HttpResponse(template.render(context))


def first(request):
	q = []
	f=open('source.txt',"r")
	content=f.readlines()
	print(content[0])
	for ch in content[0]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
	if request.method == 'POST':
		form = First(request.POST)
	else:
		form = First()
		

	return render(request, 'first.html', {'form':form, 'content':q})



