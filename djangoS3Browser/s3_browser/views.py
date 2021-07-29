import json

from django.http import HttpResponse

from .operations import *

"fetch the directories within the selected folder"


def get_folder_items(request, main_folder, sort_a_z):
    json_string = get_folder_with_items(main_folder, sort_a_z)
    return HttpResponse(json.dumps(json_string), content_type="application/json")


def upload(request):
    file = request.FILES.get('file')
    upload_file(request.POST['loc'], file)
    return HttpResponse(json.dumps(file.name), content_type="application/json", status=200)


def create_folder(request):
    create_folder_item(request.POST['loc'], request.POST['folder_name'])
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)


def download(request):
    file = request.GET.get('file')
    result = download_file(file)
    response = HttpResponse(result['Body'].read())
    response['Content-Type'] = result['ContentType']
    response['Content-Length'] = result['ContentLength']
    response['Content-Disposition'] = 'attachment; filename=' + file
    response['Accept-Ranges'] = 'bytes'
    return response


def rename_file(request):
    file_name = rename(request.POST['loc'], request.POST['file'], request.POST['new_name'])
    return HttpResponse(json.dumps(file_name), content_type="application/json", status=200)


def paste_file(request):
    paste(request.POST['loc'], request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)


def move_file(request):
    move(request.POST['loc'], request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)


def delete_file(request):
    delete(request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)
