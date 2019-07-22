from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.

def home_image(request):
    date = dt.date.today()
    photoz = Image.new_images()
    return render(request, 'mainz/content.html', {"date": date,"photoz":photoz})





def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'mainz/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'mainz/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"mainz/image.html", {"image":image})


