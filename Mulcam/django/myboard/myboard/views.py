from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone

def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all().order_by('-id')})

def insert_form(request):
    return render(request, 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def update_form(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


# 각 값을 받아서 수정해 templates에 보내주는 과정
def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)

    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_content == 2:  # 내가 원하는대로 동작했다면
        return redirect('/detail/' + id)  # 디테일로 가고
    else:  # 그게 아니라면
        return redirect('/updateform/' + id)  # 직전으로 돌아가라

def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()
	# id가 같은 객체의 queryset을 delete()해주고 result_delete에 저장
    # print(result_delete)
    if result_delete[0]: # result_delete는 튜플형태(,)
        return redirect('index')
    else:
        return redirect('detail/'+id)