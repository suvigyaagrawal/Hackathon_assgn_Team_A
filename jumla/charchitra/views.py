import datetime

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.views import generic

from django.http import HttpResponse, HttpResponseRedirect

from login.models import User
from .models import *


# Create your views here.
def dashboard(request, user_id):
    return render(request, 'charchitra/dashboard.html', {'user_id': user_id})


def VideoListView(request, user_id):
    video_list = []
    if request.method == "GET":
        try:
            if request.GET.get('filter_actor') or request.GET.get('filter_genre'):
                if len(request.GET.get('filter_actor')) > 0 and len(request.GET.get('filter_genre')) > 0:
                    # print(len(request.GET['filter_actor']) > 0 and len(request.GET['filter_genre']) > 0)
                    video_list = Video.objects.filter(a_id__a_name=request.GET['filter_actor'],
                                                      g_id__g_name=request.GET['filter_genre'])
                elif len(request.GET.get('filter_actor')) > 0:
                    video_list = Video.objects.filter(a_id__a_name=request.GET['filter_actor'])
                elif len(request.GET.get('filter_genre')) > 0:  # WIP
                    # print(len(request.GET['filter_actor']) > 0)
                    video_list = Video.objects.filter(g_id__g_name=request.GET['filter_genre'])
                    print(video_list)
                elif 'search_data' in request.GET:
                    video_list = Video.objects.filter(v_name__contains=request.GET['search_data'])
            else:
                video_list = Video.objects.all()
        except (Actor.DoesNotExist, Genre.DoesNotExist) as e:
            print('Data not found')
    print(video_list)
    video_price_list = VideoPrice.objects.all()
    template_name = 'charchitra/video_list.html'

    context = {
        'video_list': video_list,
        'video_price_list': video_price_list,
        'user_id': user_id,
    }
    return render(request, template_name, context)


def VideoDetailView(request, user_id, video_id, video_price=None):
    video_detail = get_object_or_404(Video, pk=video_id)
    video_price_detail = VideoPrice.objects.filter(v_id=video_id)
    if request.method == "GET":
        if "id-btn" in request.GET:
            # user = User.objects.get(id=id)
            print(request.GET.get("id-btn").split(" "))
            # video = Video.objects.get(v_name=request.GET.get('id-btn').split(" ")[0])
            video = Video.objects.get(pk=video_id)
            video_price = VideoPrice.objects.get(v_id=video_id,
                                                 v_price=int(float(request.GET.get('id-btn').split(" ")[1])))
            user = User.objects.get(u_id=user_id)
            subscribe = Subscribe(u_id=user, is_pack=True, v_id=video, price=video_price.v_price,
                                  dur_name=video_price.dur_name, subscription_time=datetime.datetime.now())
            with transaction.atomic():
                if Subscribe.objects.filter(pk=subscribe.pk).exists():
                    return HttpResponse('Already Subscribed')
                else:
                    subscribe.save()
                    return redirect('charchitra:video_list', user_id=user_id)
        else:
            template_name = 'charchitra/video_detail.html'
            context = {
                'user_id': user_id,
                'video_detail': video_detail,
                'video_price_detail': video_price_detail,
            }
        return render(request, template_name, context)


# def VideoPackListView(request):
# 	HttpResponse("Welcome to Video Packs.")

def VideoPackListView(request, user_id):
    video_list = Video.objects.all()
    print("Video List = ", video_list)
    video_price_list = VideoPrice.objects.all()
    print("Video Price List = ",video_price_list)
    video_pack_list = VideoPackPrice.objects.all()
    print("Video Pack Price List = ",video_pack_list)

    template_name = 'charchitra/videopack_list.html'
    context = {
        'user_id': user_id,
        'video_list': video_list,
        'video_price_list': video_price_list,
        'video_pack_list' : video_pack_list,
    }
    return render(request, template_name, context)


def UserProfileView(request, user_id):
    user = get_object_or_404(User, u_id=user_id)
    subscription_list = Subscribe.objects.filter(u_id=user)
    q_list = []
    for subs in subscription_list:
        q_list.append(subs)
    context = {
        'user_id': user_id,
        'subscription_list': subscription_list,
    }
    return render(request, 'charchitra/user_profile.html', context)
