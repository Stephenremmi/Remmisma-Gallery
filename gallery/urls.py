from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^search/", views.search, name="search_results"),
    url(r"^browse/$", views.browse, name="browse"),
    url(r"^category/(\d+)", views.category_filter, name="category"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)