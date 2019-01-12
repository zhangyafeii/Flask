from django.shortcuts import render,HttpResponse,redirect

from django import forms
from django.forms import fields


class F1Form(forms.Form):
    username = fields.CharField(max_length=18,min_length=6,required=True,
                                error_messages={'required':'用户名不能为空','max_length':'太长了','min_length':'太短了'})
    pwd = fields.CharField(min_length=32,required=True,
                           error_messages={'required':'密码不能为空','invalid':'密码长度为32位'})
    age = fields.IntegerField(required=True,
                              error_messages={'required':'不能为空','invalid':'必须为数字'})
    email = fields.EmailField(required=True,min_length=8,
                              error_messages={'required':'邮箱不能为空','invalid':'邮箱格式错误','max_length':'最小长度为8位'})


def f1(request):
    if request.method == 'GET':
        obj = F1Form()
        return render(request,'f1.html',{'obj':obj})
    else:
        # username = request.POST.get('username')  #不能为空，长度6-18
        # pwd = request.POST.get('pwd')   #不能为空，长度32
        # email = request.POST.get('email') #不能为空，邮箱格式
        # age = request.POST.get('age')   #不能为空，数字类型
        #1.检查是否为空
        #2.检查格式是否正确

        obj = F1Form(request.POST)
        #是否全部验证成功
        if obj.is_valid():
            #用户提交的数据
            print('验证成功',obj.cleaned_data)
            return redirect('http://www.xiaohuar.com')
        else:
            print('验证失败',obj.errors)
            return render(request,'f1.html',{'obj':obj})
