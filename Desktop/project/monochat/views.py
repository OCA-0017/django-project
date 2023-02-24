import re
from django.shortcuts import render, redirect


from django.views import View

from monochat.models import Users, MonoBoards
import logging

# Create your views here.

def monochat( request ):
    return render( request, 'monochat/test.html' )

def index(request):
    request.session.clear()
    return render(request, 'monochat/index.html')

def login(request):
    request.session.clear()
    if request.method == 'POST': 
        try:
            Users.objects.get(email=request.POST['login_email'], password=request.POST['login_password'])
            userinfo = Users.objects.values('id','name').get(email=request.POST['login_email'], password=request.POST['login_password'])
            request.session['login_username'] = userinfo['name']
            request.session['user_id'] = userinfo['id']
            return redirect('homepage')
        except:
            context = {'errormessage' : "正しく入力してください"}
            return render(request, 'monochat/Login.html', context)
    return render(request, 'monochat/login.html')

def register(request):
    if request.method == 'POST':
        exist_user = Users.objects.filter(email=request.POST['register_email'])
        if  exist_user: #既にメールアドレスが登録されている場合
            context = {'errormessage' : "このメールアドレスは既に登録されています"}
            return render(request, 'monochat/register.html', context)
        else:
            if request.POST['register_password'] == request.POST['register_re_password']:
                Users.objects.create(name = request.POST['register_username'], password = request.POST['register_password'], email = request.POST['register_email'])
                context = {'message' : "正常に登録されました"}
                Users.objects.values('name','email').get(email = request.POST['register_email'])
                #return render(request, 'monochat/register_result.html', context)

                Users.objects.get(email=request.POST['register_email'], password=request.POST['register_password'])
                userinfo = Users.objects.values('id','name').get(email=request.POST['register_email'], password=request.POST['register_password'])
                request.session['login_username'] = userinfo['name']
                request.session['user_id'] = userinfo['id']

                return redirect(to="homepage")
    context = {'errormessage' : "登録できませんでした"}
    return render(request, 'monochat/register.html', context)

def homepage(request):
    return render(request, 'monochat/homepage.html')


def boards(request):
    if request.method == 'GET':
        return render(request, 'monochat/boards.html')

def getBoardsCategory(request, category):
    if request.method == 'GET':
        try:
            # categoryの取得
            get_category = category
            # categoryで掲示板内容検索
            data = MonoBoards.objects.values('user_id', 'statement', 'created_at').filter(category = get_category)
            # user_idからユーザー名取得
            
            context = {
                'category': get_category,
                'data': data,
            }
            return render(request, 'monochat/in_boards.html', context)
        except Exception as e:
            # log保存
            logger = logging.getLogger(__name__)
            logger.info(e)
            return redirect(to="boards")
    elif request.method == 'POST':
        try:
            # get url
            url = request.path
            
            # get param
            comment = request.POST['comment']
            
            get_category = category
            print(request.session['user_id'])
            MonoBoards.objects.create(user_id = request.session['user_id'], category = get_category, statement = comment)

            return redirect(to=url)
        except Exception as e:
            # log保存
            logger = logging.getLogger(__name__)
            logger.info(e)
            return redirect(to=url)




class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "monochat/index.html")

index = IndexView.as_view()

class RoomView(View):
    def get(self, request, room_name, *args, **kwargs):
        context = {}
        context["room_name"] = room_name
        return render(request, "monochat/room.html", context)

room = RoomView.as_view()
