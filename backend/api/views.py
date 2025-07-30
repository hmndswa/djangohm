import json 
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    #request -> HttpRequest -> from Django itself
    #alternatively print(dir(request))
    #request.body
    print(request.GET)  #url query params 
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    #data['headers'] = request.headers 
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)


