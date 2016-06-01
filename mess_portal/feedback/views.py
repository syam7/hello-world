from django.shortcuts import render
from django.http import HttpResponse
from feedback.models import feedback

# Create your views here.
def feedback_index(request):
	feed_object = feedback()
	return render (request,"feedback/index.html")

def handling_data (request):
	feedback_object = feedback()
	feedback_object.subject = (request.POST['subject'])
	feedback_object.feedback_text = (request.POST['Text1'])
	feedback_object.save()
	return HttpResponse("Thanks!!!!")
