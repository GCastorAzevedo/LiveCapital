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
            context = handle_uploaded_file(request.FILES['upload_file'])
            return render(request, 'uploaddata/upload.html', { 'context': context })
    
    return HttpResponseRedirect('/')