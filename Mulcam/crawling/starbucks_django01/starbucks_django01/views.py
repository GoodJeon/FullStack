from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks02


def index(request):
    return render(request, 'index.html')

def starbucks(request):
    list_all = list()

    sido_all = starbucks02.getSiDo()
    for sido in sido_all:
        if sido == '17':
            result = starbucks02.getStore(sido_cd=sido)
            # print(result)
            list_all.extend(result)
        else:
            gugun_all = starbucks02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbucks02.getStore(gugun_cd=gugun)
                # print(result)
                list_all.extend(result)

    # print(list_all)
    # print(len(list_all))

    result_dict = dict()
    result_dict['list'] = list_all

    return JsonResponse(result_dict)