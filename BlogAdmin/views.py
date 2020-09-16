from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from BlogAdmin import models
import json
# 将Queryset转换成dict
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    result = [
        {
            'name': '小名',
            'age': 15
        },
        {
            'name': '小红',
            'age': 17
        },
    ]

    return HttpResponse(result, content_type="application/json")


def articles(request):
    return HttpResponse("1111")


def test(request):
    # 判断请求方法，并获取请求的参数
    if request.method == "GET":
        # id = request.GET['id']
        bloginfo = models.Blog.objects.all().values()
        data = {}
        data["data"] = list(bloginfo)
        return JsonResponse(data, safe=False)


def detail_data(request):
    if request.method == "GET":
        data = {}
        try:
            id = request.GET['id']
            data['status'] = "success"
            data['data'] = list(models.Blog.objects.filter(id=id).values())
            if len(data['data']) == 0:
                print(id)
                data['data'] = ['无此文章']
                return JsonResponse(data, safe=False)
            return JsonResponse(data, safe=False)
        except:
            data['status'] = "fail"
            data['data'] = ['参数请求异常']
            return JsonResponse(data, safe=False)


def head_img(request):
    data = {}
    if request.method == "GET":
        data['status'] = 'success'
        data['data'] = list(models.HeadImage.objects.all().values())
        return JsonResponse(data, safe=False)


def postreq(request):
    if request.method == "POST":
        print(json.loads(request.body.decode())['id'])
        print("POST请求")
        return HttpResponse("POST")
    else:
        print("GET请求")
        return HttpResponse("GET")