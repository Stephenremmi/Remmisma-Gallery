from django.shortcuts import render, redirect
from gallery.models import Photo, Location,Category

# Create your views here.
def index(request):
    photos = Photo.show_all_photos()
    return render(request, "gallery/index.html", context={"photos":photos})

def search(request):
    
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_photos = Photo.search_photo_by_category(search_term)
        results = len(searched_photos)
        message = "{}".format(search_term)
        
        return render(request, "gallery/search.html", context={"message":message,
                                                               "photos":searched_photos,
                                                               "results":results})
    else:
        message = "You have not searched for any photo"
        return render(request, "gallery/search.html", context={"message":message})

def browse(request):
    photos = Photo.show_all_photos()
    categories = Category.objects.all()
    return render(request, "gallery/browse.html", context={"photos":photos,
                                                           "categories":categories})

def category_filter(request, id):
    photos = Photo.objects.filter(categories__id = id)
    results = len(photos)
    category = Category.objects.get(id = id)
    categories = Category.objects.all()

    return render(request, "gallery/category.html", context={"photos":photos,
                                                             "results":results,
                                                             "category":category,
                                                             "categories":categories})
