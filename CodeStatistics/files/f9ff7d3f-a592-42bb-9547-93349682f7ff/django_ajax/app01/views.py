import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from app01.models import *
# Create your views here.


def students(request):
    stu_list = Students.objects.all()
    cls_list = Classes.objects.all()
    return render(request,'students.html',{'stu_list':stu_list,'cls_list':cls_list})


def add_student(request):
    response = {'status':True,'message':None,'data':None}
    try:
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls')
        obj = Students.objects.create(username=username,age=age,gender=gender,cs_id=cls_id)
        response['data'] = obj.id
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'
    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)


def del_student(request):
    result = {'status':True}
    try:
        nid = request.GET.get('nid')
        Students.objects.filter(id=nid).delete()
    except:
        result['status'] = False
    result = json.dumps(result)
    return HttpResponse(result)


def edit_student(request):
    print(request.POST)
    response = {'code':1000,'message':None}
    try:
        nid = request.POST.get('nid')
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs_id  = request.POST.get('cls')
        Students.objects.filter(id=nid).update(
            username=username,
            age=age,
            gender=gender,
            cs_id=cs_id
        )
    except Exception as e:
        response['code'] = 1001
        response['message'] = str(e)
    response = json.dumps(response)
    return HttpResponse(response)


def index(request):
    return render(request,'index.html')


def ajax1(request):
    print(request.GET)
    print(request.POST)
    # print(request.body)
    print(request.FILES)
    ret = {'status':True,'message':'ok'}
    return HttpResponse(json.dumps(ret))


def upload(request):
    return render(request,'upload.html')


def upload_img(request):
    import uuid

    nid = str(uuid.uuid4())
    ret = {'status':True,'data':None,'message':None}

    obj = request.FILES.get('k3')
    file_path = os.path.join('static',nid+obj.name)
    f = open(file_path,'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    ret['data'] = file_path
    return HttpResponse(json.dumps(ret))


def jsonp(request):
    return render(request,'jsonp.html')


def ajax3(request):
    return HttpResponse('本服务器发送的请求！')

