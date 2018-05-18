from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.template import Context, loader
from anagramsapp.forms import First
from django.views.generic.edit import FormView
import enchant

# Create your views here.


def index(request):
	'''f=open('easy.txt',"r")
	content=f.readlines()
	print(content)
	context={'content': content}

	# template = loader.get_template('index.html')'''
	return render(request, 'home.html')

	# return HttpResponse(template.render(context))




def logic(ip):
	d = enchant.Dict("en_US")
	q = []
	# for i in range(0,15):
	# 	q.append(" ")
	score = 0
	f=open('easy.txt',"r")
	# content=f.readlines()
	content = f.read()
	temp = content.split('\n')
	# print(content[0])
	print(temp)
	for ch in content[0]:
		q.append(ch)
	print(q)
	context={'content': content}
	# form = First()
	# if request.method == 'POST':
	# 	form = First(request.POST)

		# if form.is_valid():
		# 	ip = form.cleaned_data['answer']
	c = len(ip)
	for ch in ip:
		if ch in q:
			flag =True
		else:
			flag = False

		if flag == True:
			if( d.check(ip) == True):
				score = c
			else:
				score = 0
	# print(score)
	# print(q)
	# return score,q
	return q,score



def easy_first(request):
	tot_score=0
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('easy.txt',"r")
	content=f.readlines()
	print(content[0])
	for ch in content[0]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score=tot_score+score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/2/')
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'first.html', {'form':form , 'content':q, 'score':score, 'total':tot_score})


def easy_second(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('easy.txt',"r")
	content=f.readlines()
	print(content[1])
	for ch in content[1]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/3/')
				else:
					score = 0
		print(q)
		print(score)
		i=3
		# pk = pk+1

	else:
		form = First()

	return render(request, 'second.html', {'form':form , 'content':q, 'score':score, 'total':request.session['tot_score']})

def easy_third(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('easy.txt',"r")
	content=f.readlines()
	print(content[2])
	for ch in content[2]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/4/')
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'third.html', {'form':form , 'content':q, 'score':score, 'total':request.session['tot_score']})

def easy_fourth(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('easy.txt',"r")
	content=f.readlines()
	print(content[3])
	for ch in content[3]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/5/')
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'fourth.html', {'form':form , 'content':q, 'score':score, 'total':request.session['tot_score']})

def easy_fifth(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('easy.txt',"r")
	content=f.readlines()
	print(content[4])
	for ch in content[4]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					print(tot_score)
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'fifth.html', {'form':form , 'content':q, 'score':score, 'total':tot_score})


def med_first(request):
	tot_score=0
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('medium.txt',"r")
	content=f.readlines()
	print(content[0])
	for ch in content[0]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score=tot_score+score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/2/')
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'med_first.html', {'form':form , 'content':q, 'score':score, 'total':tot_score})


def med_second(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('medium.txt',"r")
	content=f.readlines()
	print(content[1])
	for ch in content[1]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/3/')
				else:
					score = 0
		print(q)
		print(score)
		i=3
		# pk = pk+1

	else:
		form = First()

	return render(request, 'med_second.html', {'form':form , 'content':q, 'score':score, 'total':request.session['tot_score']})


def med_third(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('medium.txt',"r")
	content=f.readlines()
	print(content[2])
	for ch in content[2]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/4/')
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'med_third.html', {'form':form , 'content':q, 'score':score, 'total':request.session['tot_score']})


def med_fourth(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('medium.txt',"r")
	content=f.readlines()
	print(content[3])
	for ch in content[3]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					request.session['tot_score']=tot_score
					#return HttpResponseRedirect('/5/')
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'med_fourth.html', {'form':form , 'content':q, 'score':score, 'total':request.session['tot_score']})

def med_fifth(request):
	tot_score=request.session['tot_score']
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('medium.txt',"r")
	content=f.readlines()
	print(content[4])
	for ch in content[4]:
		q.append(ch)
	print(q)
	context={'content': content}
	form = First()
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

			if flag == True:
				if( d.check(ip) == True):
					score = c
					tot_score = tot_score + score
					print(tot_score)
				else:
					score = 0
		#print(q)
		#print(score)

		# pk = pk+1

	else:
		form = First()

	return render(request, 'med_fifth.html', {'form':form , 'content':q, 'score':score, 'total':tot_score})

def finish(request):
	return render(request,'finish.html')
