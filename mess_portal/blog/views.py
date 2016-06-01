from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Question,Answer
from django.utils import timezone
from django.contrib.auth import authenticate,login    
from django.views.generic import View
from .forms import UserForm
# Create your views here.

def index(request):
	all_questions = list(Question.objects.all())
	context ={'all_questions':all_questions}
	return render (request,"blog/index.html",context)
def detail(request,question_id):
	question = Question.objects.get(id=question_id)
	all_answers = question.answer_set.all()
	context = {'question':question,
		   'all_answers':all_answers,}
	return render (request,"blog/answer.html",context)
def handling(request,question_id):
	question = Question.objects.get(id=question_id)
	answer = Answer()
	answer.answer_text = (request.POST['Text1'])
	answer.question = question
	answer.save()
	all_answers = question.answer_set.all()
	context = {'question':question,
		   'all_answers':all_answers,}
	return render (request,"blog/answer.html",context)
def add_question(request):
	question = Question()
	question.question_text=(request.POST['Text1'])
	question.pub_date = timezone.now()
	question.save()
	all_questions = list(Question.objects.all())
	context ={'all_questions':all_questions}
	return render (request,"blog/index.html",context)

	
def register(request):
	registered=False

	if request.method == 'POST'
		
		user_form=UserForm(request.POST)

	if form.is_valid():

		user=user_form.save(commit=False)
		user.set_password(password)
		user.save()
		registered = True
.......................................
		user=authenticate(username=username,password=password)

		if user is not None:

			if user.is_active:
				login(request,user)
				return redirect('blog:index')

		return render(request,self.template_name,{'form':form})