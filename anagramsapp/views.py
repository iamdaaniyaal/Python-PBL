from django.shortcuts import render,redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from anagramsapp.forms import First
from django.views.generic.edit import FormView
import enchant

from django.urls import reverse
# Create your views here.

def index(request):
	f=open('source.txt',"r")
	content=f.readlines()
	print(content)
	context={'content': content}
	
	# template = loader.get_template('index.html')
	return render(request, 'home.html', context)

	# return HttpResponse(template.render(context))




# def logic(ip):
# 	d = enchant.Dict("en_US")
# 	q = []
# 	# for i in range(0,15):
# 	# 	q.append(" ")
	
# 	f=open('source.txt',"r")
# 	# content=f.readlines()
# 	content = f.read()
# 	temp = content.split('\n')
# 	# print(content[0])
# 	print(temp)
# 	for ch in content[0]:
# 		q.append(ch)
# 	print(q)
# 	context={'content': content}
# 	# form = First()
# 	# if request.method == 'POST':
# 	# 	form = First(request.POST)

# 		# if form.is_valid():
# 		# 	ip = form.cleaned_data['answer']
# 	c = len(ip)
# 	score = c
# 	for ch in ip:
# 		if ch in q:
# 			flag =True
# 		else:
# 			flag = False

# 		if flag == True:
# 			if( d.check(ip) == True):
# 				score = c
# 			else:
# 				score = 0
# 	# print(score)
# 	# print(q)
# 	# return score,q
# 	return q,score 



def first(request,id):
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('source.txt',"r")
	content=f.readlines()
	print(content[id-1])
	for ch in content[id-1]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
	print(id)
	if request.method == 'POST':
		form = First(request.POST)

		if form.is_valid():
			ip = form.cleaned_data['answer']
			# var = list(logic(ip))
			# q.append(var[0])
			# score=var[1]
			#q=logic(ip)
			# score=score

			c = len(ip)
			
			for ch in ip:
				if ch in q:
					flag =True
				else:
					flag = False
					if flag==False:
						break

			if flag == True:
				if( d.check(ip) == True):
					score = score + c
				else:
					score =0
		print(q)
		print(score)
		print(id)

		# pk = pk+1




	else:
		form = First()
	return render(request, 'first.html', {'form':form , 'content':q, 'score':score, 'id':id+1})
	# return redirect(first,id+1,{'form':form , 'content':q, 'score':score, 'id':id+1})
	# return HttpResponseRedirect(first)

# def second(request):
# 	d = enchant.Dict("en_US")
# 	q = []
# 	# # for i in range(0,15):
# 	# # 	q.append(" ")
# 	score = 0
# 	f=open('source.txt',"r")
# 	content=f.readlines()
# 	print(content[1])
# 	for ch in content[1]:
# 		q.append(ch)
# 	print(q)
# 	context={'content': content}
# 	form = First()
# 	print(id)
# 	if request.method == 'POST':
# 		form = First(request.POST)

# 		if form.is_valid():
# 			ip = form.cleaned_data['answer']
# 			# var = list(logic(ip))
# 			# q.append(var[0])
# 			# score=var[1]
# 			#q=logic(ip)
# 			# score=score

# 			c = len(ip)
# 			for ch in ip:
# 				if ch in q:
# 					flag =True
# 				else:
# 					flag = False

# 			if flag == True:
# 				if( d.check(ip) == True):
# 					score = c
# 				else:
# 					score = 0
# 		print(q)
# 		print(score)
# 		i=3

# 		# pk = pk+1





	# else:
	# 	form = First()
	# 	print(id)


	# return render(request, 'first.html', {'form':form , 'content':q, 'score':score, 'id':id})



