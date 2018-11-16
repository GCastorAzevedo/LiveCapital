import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import UploadFileForm
from .handlers.upload import handle_uploaded_file

def index(request):
    context = {
        'input_file_id': 'id_upload_file',
        'input_file_name': 'upload_file'  
    }
    return render(request, 'uploaddata/index.html', context)

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        content = ""
        if form.is_valid():
            #content = handle_uploaded_file(request.FILES['upload_file'])
            content = request.FILES['upload_file']
            return render(request, 'uploaddata/upload.html', { 'content': content })
    
    return HttpResponseRedirect('/')

"""
print('hi')
            #if status:
            #    return HttpResponseRedirect('/insert/succes/')
            #else:
            #    return HttpResponseRedirect('/insert/')

def detail(request, id):
    response = "Look this nice detail %s."
    return HttpResponse(response % id)

def results(request, id):
    response = "This is a nice id: %s."
    return HttpResponse(response % id)

def insert(request):
    #body_unicode = request.body.decode('utf-8')
    #body = json.loads(body_unicode)
    #content = body['content']
    response = request.body
    body = json.loads(response)
    #file_ = request.FILE
    message = "see the values found \n \n %s \n \n %s" 
    
    return HttpResponse(message % (body))

"""
