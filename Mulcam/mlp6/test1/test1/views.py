from django.shortcuts import render, redirect
from django.http import HttpRequest
import math

import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from django.views.decorators.csrf import csrf_exempt
from numpyencoder import NumpyEncoder
import json
from django.http import JsonResponse

'''데이터 읽기'''
PATH='C:/projects/FullStack/Mulcam/mlp6/test1/static/data'
sp=pd.read_csv(PATH+'/서울시 우리마을가게 상권분석서비스(상권-생활인구).csv',encoding='cp949')
income_21=pd.read_csv(PATH+'/서울시 우리마을가게 상권분석서비스(상권-추정매출).csv',encoding='cp949')
income_20=pd.read_csv(PATH+'/서울시우리마을가게상권분석서비스(상권-추정매출)_2020.csv',encoding='cp949')
income_19=pd.read_csv(PATH+'/서울시 우리마을가게 상권분석서비스(상권-추정매출)_2019.csv',encoding='cp949')
income_18=pd.read_csv(PATH+'/서울시 우리마을가게 상권분석서비스(상권-추정매출)_2018.csv',encoding='cp949')

where=pd.read_csv(PATH+'/서울시 우리마을가게 상권분석서비스(상권영역).csv',encoding='cp949')
gu_code=pd.read_csv(PATH+'/행정동코드_매핑정보_2018.csv')
moneymoney=pd.read_csv(PATH+'/moneypower.csv')


'''생활 인구 데이터 전처리'''
where=where.drop(['형태정보'],axis=1)

# 시군구 코드로 where  inner join
# 기준이 되는 colum 이름을 동일하게 하여 merge 할 수 있게함

gu_code.rename(columns={'RESD_CD':'시군구_코드','RESC_CT_NM':'시군구_명'},inplace=True)
guwhere=where.merge(gu_code[['시군구_코드','시군구_명']], how='inner', on =['시군구_코드'])

# sp데이터 중 원하는 컬럼만 사용(요일 까지만)
want=sp.columns.unique()[:28]
sp_all=sp[want]


# 구, x좌표, y좌표 join한 생활인구 데이터
sp_all=sp_all.merge(guwhere[['상권_코드','시군구_명','엑스좌표_값','와이좌표_값']],how='inner',on='상권_코드')

#기준 년코드 2018년도 이상인 것만 사용
sp_all=sp_all[sp_all['기준 년코드']>=2018]

# sp_recent(최근 1년)
sp_recent=sp_all[((sp_all['기준 년코드']==2020)&(sp_all['기준_분기_코드']==4))|(sp_all['기준 년코드']==2021)]

sp_recent['기준_분기_코드']=sp_recent['기준_분기_코드'].replace({3:'3분기',2:'2분기',1:'1분기',4:'4분기'})



''' --------------- VIEWS---------------- '''

# 처음 생활인구/상권 선택 창
def title(request):
    return render(request,'index.html')

# 구 선택 창
@csrf_exempt
def gu(request):
    bt=request.POST.get('bt')
    return render(request,'gu.html',{'bt':bt})

# 상권 선택 창
@csrf_exempt
def sangkwon(request):
    if request.method=='POST':
        print(request.POST)
        bt=request.POST['bt']
        where=request.POST['wheregu']
        a=sp_recent[sp_recent['시군구_명']==where]
        sklist=list(a['상권_코드_명'].unique())
        sklist.sort()
        v=min(math.ceil(len(sklist)**(1/2)),math.ceil(len(sklist)/(math.ceil(len(sklist)**(1/2)))))
        h=max(math.ceil(len(sklist)**(1/2)),math.ceil(len(sklist)/(math.ceil(len(sklist)**(1/2)))))

        return render(request, 'sangkwon.html', {'sklist':sklist,'v':v,'h':h, 'bt':bt,'wheregu':where})

# 생활인구 info 출력
@csrf_exempt
def pop_info(request):
    if request.method == 'POST':
        bt=request.POST['bt']
        wheregu=request.POST['wheregu']
        wheresk=request.POST['wheresk']
        
        # 구 선택 데이터
        a=sp_recent[sp_recent['시군구_명']==wheregu]
        
        # 구 + 상권 생활인구 차트용 데이터 보내기
        tmp = a[a['상권_코드_명'] == wheresk]
        ingu = (tmp['총_생활인구_수'].groupby(tmp['기준_분기_코드']).sum()).values

        # 성별 퍼센트 데이터 보내기
        male = (tmp['남성_생활인구_수'].sum())
        female = (tmp['여성_생활인구_수'].sum())
        m = int(male)
        f = int(female)
        mPer = round(m/(m+f) * 100)
        fPer = round(f/(m+f) * 100)

        # 분기 별, 요일별 총 생활인구 수
        mon = tmp['월요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        tue = tmp['화요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        wed = tmp['수요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        thu = tmp['목요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        fri = tmp['금요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        sat = tmp['토요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        sun = tmp['일요일_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values

        # 분기 별, 연령대별 총 생활인구 수
        age10 = tmp['연령대_10_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        age20 = tmp['연령대_20_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        age30 = tmp['연령대_30_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        age40 = tmp['연령대_40_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        age50 = tmp['연령대_50_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        age60 = tmp['연령대_60_이상_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values

        # 분기 별, 시간대별 총 생활 인구 수
        t1 = tmp['시간대_1_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        t2 = tmp['시간대_2_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        t3 = tmp['시간대_3_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        t4 = tmp['시간대_4_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        t5 = tmp['시간대_5_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        t6 = tmp['시간대_6_생활인구_수'].groupby(tmp['기준_분기_코드']).sum().values
        
        sknames = list(a['총_생활인구_수'].groupby(a['상권_코드_명']).mean().index)
        skvalues = list(map(int,a['총_생활인구_수'].groupby(a['상권_코드_명']).mean().values))

        return render(request, 'pop_info.html', 
        {'wheregu':wheregu,'wheresk':wheresk,'ingu':ingu, 
        'm':mPer, 'f':fPer, 'mpop':m, 'fpop':f,
        'mon':mon,'tue':tue,'wed':wed,'thu':thu,'fri':fri,'sat':sat,'sun':sun,
        'age10':age10,'age20':age20,'age30':age30,'age40':age40,'age50':age50,'age60':age60,
        't1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'sknames':sknames, 'skvalues':skvalues})

@csrf_exempt
def storepage(request):
     if request.method=='POST':
        bt=request.POST['bt']
        wheregu = request.POST['wheregu']
        wheresk = request.POST['wheresk']
        list = [
            '종로구', '중구', '용산구', '성동구', '광진구',
            '동대문구', '중랑구', '성북구', '강북구',
            '도봉구', '노원구', '은평구', '서대문구',
            '마포구', '양천구', '강서구', '구로구',
            '금천구', '영등포구', '동작구', '관악구',
            '서초구', '강남구', '송파구', '강동구']
        if wheregu in list:
            list.remove(wheregu)
            list.insert(0,wheregu)

        return render(request,'sk_info.html', {'guList': list,'bt':bt, 'wheregu':wheregu, 'wheresk':wheresk})

@csrf_exempt
def guSang(request):
    guCode = request.GET['wheregu']
    guCo= moneymoney[moneymoney['행정구_명']==guCode]
    sang= guCo['상권_코드_명'].unique()
    itsang={'sangG':sang}
    itsang=(json.dumps(itsang, cls=NumpyEncoder, indent=4, ensure_ascii=False))
    return JsonResponse(itsang,safe=False)

# 매출 info 출력
@csrf_exempt
def sk_info(request):
    if request.method=='POST':
        bt=request.POST['bt']
        wheregu = request.POST['wheregu']
        wheresk = request.POST['wheresk']
        if 'wheregage' in request.POST:
            wheregage = request.POST['wheregage']
            selGu=moneymoney[moneymoney['행정구_명']== wheregu]

            gud = selGu[(selGu['상권_코드_명']== wheresk)&(selGu['서비스_업종_코드_명']== wheregage)]
            # print(gud)
            # 성별 퍼센트 데이터 보내기
            male = (gud['남성_매출_금액'].sum())
            print(male)
            female = (gud['여성_매출_금액'].sum())
            m = int(male)
            f = int(female)
            mPer = round(m / (m + f) * 100)
            fPer = round(f / (m + f) * 100)

            # 분기 별, 요일별 총 생활인구 수
            mon = gud['월요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            tue = gud['화요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            wed = gud['수요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            thu = gud['목요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            fri = gud['금요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            sat = gud['토요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            sun = gud['일요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values

            jumpo = gud['점포수'].groupby(gud['기준_분기_코드']).sum().values

            # 분기 별, 연령대별 총 생활인구 수
            age10 = gud['연령대_10_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            age20 = gud['연령대_20_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            age30 = gud['연령대_30_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            age40 = gud['연령대_40_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            age50 = gud['연령대_50_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            age60 = gud['연령대_60_이상_매출_금액'].groupby(gud['기준_분기_코드']).sum().values


            # 분기 별, 시간대별 총 생활 인구 수
            t1 = gud['시간대_00~06_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            t2 = gud['시간대_06~11_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            t3 = gud['시간대_11~14_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            t4 = gud['시간대_14~17_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            t5 = gud['시간대_17~21_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
            t6 = gud['시간대_21~24_매출_금액'].groupby(gud['기준_분기_코드']).sum().values


            result ={'bt':bt,'wheregu': wheregu,'wheresk':wheresk,'wheregage':wheregage, 'm': mPer, 'f': fPer,'mon': mon, 'tue': tue, 'wed': wed, 'thu': thu, 'fri': fri, 'sat': sat, 'sun': sun,'age10': age10, 'age20': age20, 'age30': age30, 'age40': age40, 'age50': age50, 'age60': age60,'t1': t1, 't2': t2, 't3': t3, 't4': t4, 't5': t5, 't6': t6, 'jumpo':jumpo}
            result =(json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))
            return JsonResponse(result,safe=False)

def showlist(request):
    return render(request,'showlist.html')