from django.shortcuts import render, redirect, reverse, HttpResponse
from ..login_reg.models import User
from models import Friend
# Create your views here.
def index(request):
    sessionid=request.session['id']
    lstfriend = User.objects.exclude(userfriend__sessionuser_id=sessionid).exclude(id=sessionid)
    context = {
    'all_users' : lstfriend,
    'all_friends' : Friend.objects.filter(sessionuser_id=sessionid)
    }
    return render(request, 'friend/index.html', context)

def user_info(request, user_id):
    context = {
    'user' : User.objects.filter(id=user_id)
    }
    return render(request, 'friend/userinfo.html', context)

def add_friend(request, friend_id):
    sessionid = request.session['id']
    user = User.objects.get(id=sessionid)
    friend = User.objects.get(id=friend_id)
    Friend.objects.create(sessionuser=user, friend=friend)
    Friend.objects.create(sessionuser=friend, friend=user)
    return redirect('friend:index')

def remove_friend(request, friendship_id):
    Friend.objects.get(id=friendship_id).delete()
    return redirect('friend:index')
