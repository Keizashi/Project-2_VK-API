import json
from django.http import HttpResponse, JsonResponse
import requests


def Index(request, vkid):
    dict = requests.get('https://api.vk.com/method/users.get?v=5.73&user_ids=' + str(vkid) + '&fields=photo_50')

    data = {
        "vk_data": {
            "id": vkid,
            "first_name": dict.json()['response'][0]['first_name'],
            "last_name":  dict.json()['response'][0]['last_name'],
            "photo_url":  dict.json()['response'][0]['photo_50']
        }
    }
    return JsonResponse(data, safe=False)
