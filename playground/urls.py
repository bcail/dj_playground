from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home_view(request):
    page = '<html><body><p><a href="polls/">Polls</a></p><p><a href="admin/">Admin</a></p>'
    return HttpResponse(page)


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', home_view),
]
