import json

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

from .models import MediaDate


class MediaView(View):
    def get(self,request,method,*args,**kwargs):
        try:
            if method=='save':
                filename= request.GET.get('filename',None)
                majortype= request.GET.get('majortype',None)
                minortype= request.GET.get('minortype',None)
                value= request.GET.get('value',None)
                domain= request.GET.get('domain',None)
                new_media_object = MediaDate(filename=filename,majortype=majortype,minortype=minortype,value=value,domain=domain)
                new_media_object.save()
            elif method == 'update':
                old_value = request.GET.get('old_value')
                if old_value==None:
                    return HttpResponse(content_type='application/json;charset=utf-8',status=400,content=json.dumps({'error':"miss value for object"}))
                else:
                    old_object = MediaDate.objects.get(value=old_value)
                    if old_value ==None:
                        return HttpResponse(content_type='application/json;charset=utf-8', status=400,
                                            content=json.dumps({'error': "don't have value for object"}))
                    filename = request.GET.get('filename', None)
                    majortype = request.GET.get('majortype', None)
                    minortype = request.GET.get('minortype', None)
                    value = request.GET.get('value', None)
                    domain = request.GET.get('domain', None)
                    old_object.filename= filename
                    old_object.value= value
                    old_object.save()
        except Exception as e:
            print(e)
            response = HttpResponse(content_type="application/json;charset=utf-8",status=404,content=json.dumps({'status':'false'}))
            return response
        response= HttpResponse(content_type="application/json;charset=utf-8",status=200,content=json.dumps({'statue':'success'}))
        return response


    def post(self,request,*args,**kwargs):

        response = HttpResponse(content_type='application/json;charset-"utf-8"',status=200,content= json.dumps({"status":"no message"}))
        false_data = {
            "filename":"filename_false",
            "value":"value_false"

        }
        false_list = [false_data*100]
        MediaDate.save_all(false_list)
        return response











