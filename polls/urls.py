from django.urls import path
from django.conf import settings

# from django.utils.http import is_safe_url

from . import views

# if is_safe_url('/', allowed_hosts=settings.ALLOWED_HOSTS):
#     pass

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
