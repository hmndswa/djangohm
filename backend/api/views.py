import json 
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.obejcts.all().order_by("?").first() 
    #^^makes a random query set and grabs one of those values which gives model instance
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
