from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
import requests
import pandas as pd
from collections import Counter

def index(request):
    return render(request,'index.html')

def infra(request):

    return render(request, 'infra.html')


# 재원님 부분
def infra_data(request):
    infra_type = request.GET['infra']
    lst = []
    lst_year = []
    cnt_17,cnt_18,cnt_19,cnt_20 = 0,0,0,0
    if infra_type == 'InfSpeedBump':
        infra = InfSpeedBump.objects.all().order_by('-id')
    elif infra_type == 'InfSmartCross':
        infra = InfSmartCross.objects.all().order_by('-id')
    elif infra_type == 'InfSmartLamp':
        infra = InfSmartLamp.objects.all().order_by('-id')
    elif infra_type == 'InfYellowcarpet':
        infra = InfYellowcarpet.objects.all().order_by('-id')
    elif infra_type == 'InfUnCamera':
        infra = InfUnCamera.objects.all().order_by('-id')
    elif infra_type == 'InfChildZone':
        infra = InfChildZone.objects.all().order_by('-id')
    elif infra_type == 'InfEleDisplay':
        infra = InfEleDisplay.objects.all().order_by('-id')
    for i in infra:
        lst.append(i.year_code)
        # print(type(i.year_code))
        # print(i.year_code)
        if i.year_code == 17:
            cnt_17 += 1
        elif i.year_code == 18:
            cnt_18 += 1
        elif i.year_code == 19:
            cnt_19 += 1
        elif i.year_code == 20:
            cnt_20 += 1
        # print(infra)
        lst = set(lst)
        lst = list(lst)
        # print(lst_year)
        # print(lst)
        # print(infra)
        json_dict = {'17': cnt_17, '18': cnt_18, '19': cnt_19, '20': cnt_20}
        # print(json_dict)
    return JsonResponse(json_dict)

def all_infra(request):
    lst = []
    lst_obj = []
    tmp = {}
    name_lst = ['infra_sp','infra_smcro','infra_smlap','infra_yel','infra_cam','infra_chzone','infra_ele_display']
    cnt_17,cnt_18,cnt_19,cnt_20 = 0,0,0,0
    infra_sp = InfSpeedBump.objects.all().order_by('-id')
    infra_smcro = InfSmartCross.objects.all().order_by('-id')
    infra_smlap = InfSmartLamp.objects.all().order_by('-id')
    infra_yel = InfYellowcarpet.objects.all().order_by('-id')
    infra_cam = InfUnCamera.objects.all().order_by('-id')
    infra_chzone = InfChildZone.objects.all().order_by('-id')
    infra_ele_display = InfEleDisplay.objects.all().order_by('-id')


    lst_obj.append(infra_sp)
    lst_obj.append(infra_smcro)
    lst_obj.append(infra_smlap)
    lst_obj.append(infra_yel)
    lst_obj.append(infra_cam)
    lst_obj.append(infra_chzone)
    lst_obj.append(infra_ele_display)
    print('------------------------------------------------')
    # print(infra_sp)
    print('------------------------------------------------')
    # print(lst_obj)
    print('------------------------------------------------')
    for i in range(len(lst_obj)):
        for obj in lst_obj[i]:
            if obj.year_code == 17:
                cnt_17 += 1
            elif obj.year_code == 18:
                cnt_18 += 1
            elif obj.year_code == 19:
                cnt_19 += 1
            elif obj.year_code == 20:
                cnt_20 += 1
        lst.append(cnt_17)
        lst.append(cnt_18)
        lst.append(cnt_19)
        lst.append(cnt_20)
        cnt_17, cnt_18, cnt_19, cnt_20 = 0, 0, 0, 0
        tmp[name_lst[i]] = lst
        # print(tmp)
        lst = []
    # print(tmp)
    # print(lst)
    # 연도별 사망자수 + 부상자수 sum 컬럼만
    acc = InfCarAcc.objects.all().order_by('id')
    for i in acc:
        sum_cg = 0
        if (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 17:
            # print(i.sum)
            sum_cg = i.sum
        elif (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 18:

            sum_cg = i.sum
        elif (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 19:

            sum_cg+= i.sum
        elif (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 20:

            sum_cg = i.sum

        lst.append(sum_cg)

    tmp['CG'] = lst
    print(tmp)
    return JsonResponse(tmp)

# 지영님 부분
def sago_data(request):
    sago_type = request.GET['seoul_sago']
    print(sago_type)

    s_death = []
    s_hurt = []
    json_ddict = {}

    sago_years = [17, 18, 19, 20]
    count_num = ['사망자수', '부상자수']
    sago_category = ['ctoc', 'ctop', 'calone']

    if sago_type == 'CtoC':
        sago_CtoC = InfCarAcc.objects.values('cg', 'ctoc', 'year_code')

        for i in range(len(sago_years)):
            s_death.append(sago_CtoC.filter(cg=count_num[0], year_code=sago_years[i])[0]['ctoc'])
            s_hurt.append(sago_CtoC.filter(cg=f'{count_num[1]}', year_code=f'{sago_years[i]}')[0]['ctoc'])
            json_ddict[i] = s_death[i]
            json_ddict[i + 4] = s_hurt[i]

    elif sago_type == 'CtoP':
        sago_CtoP = InfCarAcc.objects.values('cg','ctop','year_code')

        for i in range(len(sago_years)):
            for _ in range(len(count_num)):
                s_death.append(sago_CtoP.filter(cg=f'{count_num[0]}', year_code=f'{sago_years[i]}')[0]['ctop'])
                s_hurt.append(sago_CtoP.filter(cg=f'{count_num[1]}', year_code=f'{sago_years[i]}')[0]['ctop'])
            json_ddict[i] = s_death[i]
            json_ddict[i + 4] = s_hurt[i]

    elif sago_type == 'CAlone':
        sago_CAlone = InfCarAcc.objects.values('cg','calone','year_code')

        for i in range(len(sago_years)):
            for _ in range(len(count_num)):
                s_death.append(sago_CAlone.filter(cg=f'{count_num[0]}', year_code=f'{sago_years[i]}')[0]['calone'])
                s_hurt.append(sago_CAlone.filter(cg=f'{count_num[1]}', year_code=f'{sago_years[i]}')[0]['calone'])
            json_ddict[i] = s_death[i]
            json_ddict[i + 4] = s_hurt[i]

    return JsonResponse(json_ddict)



# 성헌님 부분
def infPopulation_data(request):
    # 지역구별 인프라
    cross = InfSmartCross.objects.values('id', 'gugun')
    bump = InfSpeedBump.objects.values('id', 'gugun')
    carpet = InfYellowcarpet.objects.values('id', 'gugun')
    zone = InfChildZone.objects.values('id', 'gugun')
    display = InfEleDisplay.objects.values('id', 'gugun')
    lamp = InfSmartLamp.objects.values('id', 'gugun')
    camera = InfUnCamera.objects.values('id', 'gugun')

    gugun_pop = []
    gugun_list = []
    population2020 = InfPopulation.objects.filter(year_code=20).values('gugun', 'pop_sum')

    for i in range(1,len(population2020)):
        gugun_list.append(list(population2020.values('gugun')[i].values()))

    # print(gugun_list)
    # print(gugun_list[1])
    list2 = sum(gugun_list,[])
    # print(list2)
    # print(list2[1])

    print(population2020.filter(gugun=list2[1])[0]['pop_sum'])
    for j in range(0, len(list2)):
        cnt = (cross.filter(gugun=list2[j]).count()
               + bump.filter(gugun=list2[j]).count()
               + carpet.filter(gugun=list2[j]).count()
               + zone.filter(gugun=list2[j]).count()
               + display.filter(gugun=list2[j]).count()
               + lamp.filter(gugun=list2[j]).count()
               + camera.filter(gugun=list2[j]).count()
               )
        gugun_pop.append(cnt / population2020.filter(gugun=list2[j])[0]['pop_sum'])
    # print(gugun_pop)

    json_dict_gugun = {}


    for k in range(0, len(list2)):
        json_dict_gugun[list2[k]] = gugun_pop[k]

    # print(json_dict_gugun)
    return JsonResponse(json_dict_gugun)












# 동준 부분
def keyword(request):
    return render(request,'keyword.html')

def keyword_data(request):
    accident_type = request.GET['accident']
    if accident_type == 'Frequentzoneoldman':
        area = FrequentzoneoldmanKeywordsearch.objects.all().order_by('category')
    elif accident_type == 'Frequentzonetmzon':
        area = FrequentzonetmzonKeywordsearch.objects.all().order_by('category')
    elif accident_type == 'Frequentzonechild':
        area = FrequentzonechildKeywordsearch.objects.all().order_by('category')
    elif accident_type == 'Schoolzonechild':
        area = SchoolzonechildKeywordsearch.objects.all().order_by('category')
    elif accident_type == 'Jaywalking':
        area = JaywalkingKeywordsearch.objects.all().order_by('category')

    print(area[0])
    # key = ['어린이','초등학교','놀이터','키즈카페',
    # '소아과','학원','요양원','경로당',
    # '공원','IC','요금소','버스터미널',
    # '관광지','숙박업소','시장','주차장','술집']
    json_dict = {}
    json_dict['type'] = accident_type
    test = []
    for i in area:
        if i.category != 'nan' or i.category[-1] != '만':
            test.append(i.category)
        else:
            continue
    cate_name = list(Counter(test).keys())
    cate_num = list(Counter(test).values())
    key_obj = {'cate_name':cate_name, 'cate_num':cate_num}
    json_dict['keyword'] = key_obj
    # for i in key:
    #     new_area = area.filter(keyword=i)
    #     test = []
    #     for j in new_area:
    #         if j.category != 'nan':
    #             test.append(j.category)
    #         else:
    #             continue
    #     cate_name = list(Counter(test).keys())
    #     cate_num = list(Counter(test).values())
    #     key_obj = {'cate_name':cate_name,'cate_num':cate_num}
    #     json_dict[i] = key_obj
    # json_dict['key'] = key
    # print(json_dict)
    return JsonResponse(json_dict)



# 재원님 파이차트 부분
def pie(request):
    return render(request,'pie.html')


def sido_pie(request):
    lst_obj = []
    tmp_obj = {}
    childAccident = FrequentzonechildAccident.objects.all().order_by('id')
    lgAccident = FrequentzonelgAccident.objects.all().order_by('id')
    oldmanAccident = FrequentzoneoldmanAccident.objects.all().order_by('id')
    tmzonAccident = FrequentzonetmzonAccident.objects.all().order_by('id')
    Jaywalking = JaywalkingAccident.objects.all().order_by('id')
    Schoolzonechild = SchoolzonechildAccident.objects.all().order_by('id')

    lst_obj.extend([childAccident,lgAccident,oldmanAccident,tmzonAccident,Jaywalking,Schoolzonechild])
    # print(lst_obj)
    name_lst = ['보행어린이','자치구3','노인보행','연휴','무단횡단','스쿨존']
    # print(childAccident)
    cnt_seoul,cnt_busan,cnt_daegu,cnt_inch,cnt_gwan,cnt_daejeon,cnt_ulsan,cnt_sejong,cnt_gyeonggi,cnt_gang,cnt_chungN=0,0,0,0,0,0,0,0,0,0,0
    cnt_chungS,cnt_jeollaN,cnt_jeollaS,cnt_gyeonsanN,cnt_gyeonsanS,cnt_jeju = 0,0,0,0,0,0
    year_lst = [2017,2018,2019,2020]
    year_seoul, year_busan, year_daegu, year_inch, year_gwan, year_daejeon, year_ulsan, year_sejong, year_gyeonggi, year_gang, year_chungN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    year_chungS, year_jeollaN, year_jeollaS, year_gyeonsanN, year_gyeonsanS, year_jeju = 0, 0, 0, 0, 0, 0
    yearcnt = {}
    top_tmp = {}
    for i in range(len(lst_obj)):
        if i == 1:
            for YY in year_lst:
                for obj in lst_obj[1]:
                    # print(obj.address)
                    if obj.year == YY:
                        if obj.address[0:2] == '서울':
                            year_seoul += obj.occur
                        elif obj.address[0:2] == '부산':
                            year_busan += obj.occur
                        elif obj.address[0:2] == '대구':
                            year_daegu += obj.occur
                        elif obj.address[0:2] == '인천':
                            year_inch += obj.occur
                        elif obj.address[0:2] == '광주':
                            year_gwan += obj.occur
                        elif obj.address[0:2] == '대전':
                            year_daejeon += obj.occur
                        elif obj.address[0:2] == '울산':
                            year_ulsan += obj.occur
                        elif obj.address[0:2] == '세종':
                            year_sejong += obj.occur
                        elif obj.address[0:2] == '경기':
                            year_gyeonggi += obj.occur
                        elif obj.address[0:2] == '강원':
                            year_gang += obj.occur
                        elif obj.address[0:2] == '충청':
                            if obj.address[2:4] == '남도':
                                year_chungS += obj.occur
                            elif obj.address[2:4] == '북도':
                                year_chungN += obj.occur
                        elif obj.address[0:2] == '전라':
                            if obj.address[2:4] == '남도':
                                year_jeollaS += obj.occur
                            elif obj.address[2:4] == '북도':
                                year_jeollaN += obj.occur
                        elif obj.address[0:2] == '경상':
                            if obj.address[2:4] == '남도':
                                year_gyeonsanS += obj.occur
                            elif obj.address[2:4] == '북도':
                                year_gyeonsanN += obj.occur
                        elif obj.address[0:2] == '제주':
                            year_jeju += obj.occur
                yearcnt = {'서울': year_seoul, '부산': year_busan, '대구': year_daegu, '인천': year_inch, '광주': year_gwan,
                       '대전': year_daejeon, '울산': year_ulsan, '세종': year_sejong, '경기': year_gyeonggi,
                       '강원': year_gang, '충청북도': year_chungN, '충청남도': year_chungS, '전라북도': year_jeollaN, '전라남도': year_jeollaS,
                       '경상북도': year_gyeonsanN, '경상남도': year_gyeonsanS, '제주': year_jeju}
                top_tmp[YY] = yearcnt
                # print(top_tmp)
                year_seoul, year_busan, year_daegu, year_inch, year_gwan, year_daejeon, year_ulsan, year_sejong, year_gyeonggi, year_gang, year_chungN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                year_chungS, year_jeollaN, year_jeollaS, year_gyeonsanN, year_gyeonsanS, year_jeju = 0, 0, 0, 0, 0, 0
                yearcnt = {}
        for obj in lst_obj[i]:  # 여기 까지만 하면 유형별(시도로 묶을수있음)
            # print(i.address)
            if obj.address[0:2] == '서울':
                cnt_seoul += obj.occur
            elif obj.address[0:2] == '부산':
                cnt_busan += obj.occur
            elif obj.address[0:2] == '대구':
                cnt_daegu += obj.occur
            elif obj.address[0:2] == '인천':
                cnt_inch += obj.occur
            elif obj.address[0:2] == '광주':
                cnt_gwan += obj.occur
            elif obj.address[0:2] == '대전':
                cnt_daejeon += obj.occur
            elif obj.address[0:2] == '울산':
                cnt_ulsan += obj.occur
            elif obj.address[0:2] == '세종':
                cnt_sejong += obj.occur
            elif obj.address[0:2] == '경기':
                cnt_gyeonggi += obj.occur
            elif obj.address[0:2] == '강원':
                cnt_gang += obj.occur
            elif obj.address[0:2] == '충청':
                if obj.address[2:4] == '남도':
                    cnt_chungS += obj.occur
                elif obj.address[2:4] == '북도':
                    cnt_chungN += obj.occur
            elif obj.address[0:2] == '전라':
                if obj.address[2:4] == '남도':
                    cnt_jeollaS += obj.occur
                elif obj.address[2:4] == '북도':
                    cnt_jeollaN += obj.occur
            elif obj.address[0:2] == '경상':
                if obj.address[2:4] == '남도':
                    cnt_gyeonsanS += obj.occur
                elif obj.address[2:4] == '북도':
                    cnt_gyeonsanN += obj.occur
            elif obj.address[0:2] == '제주':
                cnt_jeju += obj.occur
        # print(cnt_seoul)
        tmp={'서울':cnt_seoul ,'부산':cnt_busan,'대구':cnt_daegu,'인천':cnt_inch,'광주':cnt_gwan,'대전':cnt_daejeon,'울산':cnt_ulsan,'세종':cnt_sejong,'경기':cnt_gyeonggi,
            '강원':cnt_gang,'충청북도':cnt_chungN,'충청남도':cnt_chungS,'전라북도':cnt_jeollaN,'전라남도':cnt_jeollaS,
            '경상북도':cnt_gyeonsanN,'경상남도':cnt_gyeonsanS,'제주':cnt_jeju}
        cnt_seoul, cnt_busan, cnt_daegu, cnt_inch, cnt_gwan, cnt_daejeon, cnt_ulsan, cnt_sejong, cnt_gyeonggi, cnt_gang, cnt_chungN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        cnt_chungS, cnt_jeollaN, cnt_jeollaS, cnt_gyeonsanN, cnt_gyeonsanS, cnt_jeju = 0, 0, 0, 0, 0, 0
        tmp_obj[name_lst[i]] = tmp
        tmp={}
    # print(tmp)
    tmp_obj['top'] = top_tmp
    # print(tmp_obj)
    # print(tmp_obj['보행어린이']['서울'])
    a = {'a':50000}
    return JsonResponse(tmp_obj)


