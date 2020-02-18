from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Author , News1
import json

# Create your views here.

@csrf_exempt
def postNews(request):

    if request.method == 'POST':
        body_msg = request.body.decode('utf-8')
        msg = json.loads(body_msg)
        objAuthor = Author.objects.get(id = msg['ReporterId'])
        news = News1(text = msg['text'] , date = timezone.now().strftime('%Y-%m-%d') , reporter = objAuthor)
        news.save()

        myJson = {
            "response" : str(News1.objects.filter(reporter = objAuthor))
        }
        return JsonResponse(myJson)

@csrf_exempt
def getNews(request , Date):

    if request.method == 'GET':

        akhbar_list = []
        akhbar = News1.objects.filter(date = str(Date))

        for i in akhbar:
            akhbar_list.append({'Author' : i.reporter.name , 'Text' : i.text , 'Date' : str(i.date)})

        myJson = {
            "KHABAR" : akhbar_list
        }    

        return JsonResponse(myJson)   

@csrf_exempt
def putNews(request , report_id):
    
    if request.method == 'PUT':

        khabar = News1.objects.get(id = report_id)
        body_msg = request.body.decode('utf-8')
        msg = json.loads(body_msg)

        khabar.text = msg['text']
        khabar.save()

        khabarnegar = khabar.reporter
        myJson = {"response" : str(News1.objects.filter(reporter = khabarnegar))}
        return JsonResponse(myJson)

@csrf_exempt
def delNews(request , iD):

    if request.method == 'DELETE':
        
        try:
            khabar = News1.objects.get(id = iD)
            khabar.delete()

            repid = khabar.reporter
            myJson = {"response" : str(News1.objects.filter(reporter = repid))}

        except Exception as e:
            myJson = {"error" : str(e)}

        return JsonResponse(myJson)









