from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.template import Context, loader
from anagramsapp.forms import First
from django.views.generic.edit import FormView
import enchant

# Create your views here.

def index(request):
	'''f=open('source.txt',"r")
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
	f=open('source.txt',"r")
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



def first(request,id):
	d = enchant.Dict("en_US")
	q = []
	# tot_score = 0
	a = " "
	id=int(id)
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
	f=open('source.txt',"r")
	content=f.readlines()
	# print(content[0])
	try:
		for ch in content[id-1]:
			q.append(ch)
	except IndexError:
		return render(request,'final.html')

	print(content[id-1])
	# context={'content': content}
	# if(content[id-1] == " ") :
	# 	return render(request, 'final.html')


	form = First()
	if request.method == 'POST':
		form = First(request.POST)
<<<<<<< HEAD
		if form.is_valid():
			ip = form.cleaned_data['answer']
			# var = list(logic(ip))
			# q.append(var[0])
			# score=var[1]
			#q=logic(ip)
			# score=score

			c = len(ip)
			print("input is ",ip)
			for ch in ip:
				print(ch)
				print(content[id-1])
				if ch or ch.upper() or ch.lower() in content[id-1]:
					flag =True
					print(flag)
				else:
					flag = False
					print(flag)
					a="Not a Anagram"
					return render(request, 'final.html')

			if flag == True:
				if( d.check(ip) == True):
					score = c
					# tot_score =tot_score+score
					# request.session['total']=tot_score
					# print("tot is",tot_score)

					a="It is an Anagram"
				else:
					score = 0
					a="Not a Anagram"
					return render(request, 'final.html')
		#print(q)
		print(score)

		# pk = pk+1





	else:
		form = First()
		return render(request, 'first1.html', {'form':form , 'content':content[id-1], 'score':score, 'id':id+1, 'a':a, 'idi':id+2})

	print("id is",id)
	if(id>10):
		return redirect(done)

	return render(request, 'first.html', {'form':form , 'content':content[id-1], 'score':score, 'id':id+1, 'a':a, 'idi':id+2})



def first1(request,id):
	print("score is" ,score)
	# tot_score=request.session['total']
	d = enchant.Dict("en_US")
	q = []
	a = " "
	# # for i in range(0,15):
	# # 	q.append(" ")
	# score = 0
	f=open('source.txt',"r")
	content=f.readlines()
	# print(content[0])
	for ch in content[id-1]:
		q.append(ch)
	print(content[id-1])
	# context={'content': content}
	form = First()
	if request.method == 'POST':
		form = First(request.POST)
=======
>>>>>>> fdcf26859832fc2ace3786be46a62b53d0e97353
		if form.is_valid():
			ip = form.cleaned_data['answer']
			# var = list(logic(ip))
			# q.append(var[0])
			# score=var[1]
			#q=logic(ip)
			# score=score

			c = len(ip)
			print("input is ",ip)
			for ch in ip:
				print(content[id-1])
				if ch or ch.lower() in content[id-1]:
					flag =True
					print(flag)
				else:
					flag = False
					print(flag)
					a="Not a Anagram"
					return render(request, 'final.html')

			if flag == True:
				if( d.check(ip) == True):
					score = c
					# tot_score=tot_score+score
					# print("tot is",tot_score)
					a="It is an Anagram"
				else:
					score = 0
<<<<<<< HEAD
					a="Not a Anagram"
					return render(request, 'final.html')
		#print(q)
		print(score)
=======
		#print(q)
		#print(score)
>>>>>>> fdcf26859832fc2ace3786be46a62b53d0e97353

		# pk = pk+1





	else:
		form = First()


	return render(request, 'first1.html', {'form':form , 'content':content[id-1], 'score':score, 'id':id+1, 'a':a, 'idi':id+2})


def second(request):
	d = enchant.Dict("en_US")
	q = []
	# # for i in range(0,15):
	# # 	q.append(" ")
	score = 0
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

		if form.is_valid():
			ip = form.cleaned_data['answer']
			# var = list(logic(ip))
			# q.append(var[0])
			# score=var[1]
			#q=logic(ip)
			# score=score

			c = len(ip)
			for ch in ip:
				print(q)
				if ch in q:
					flag =True
				else:
					flag = False

			if flag == True:
				if( d.check(ip) == True):
					score = c
				# else:
				# 	score = 0
		print(q)
		print(score)
		# pk = pk+1





	else:
		form = First()
	print("id is",id)
	if(id>10):
		return redirect(done)


	return render(request, 'first.html', {'form':form , 'content':q, 'score':score,'i': i})



def done(request):
	return render(request, 'done.html')