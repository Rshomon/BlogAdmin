from django.shortcuts import render, HttpResponse
import json


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

    return HttpResponse(result,content_type="application/json" )


def articles(request):
    return HttpResponse("1111")
