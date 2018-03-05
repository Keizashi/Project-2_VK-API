import json
from django.http import HttpResponse, JsonResponse

# def Index(request, vkid):
#     json_object = {'vkid': '1'}
#     return JsonResponse(json_object)

def your_view(request, vkid):
    json_object = {'key': vkid}
    return JsonResponse(json_object)