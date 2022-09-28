from django.urls import URLPattern, path

from .views import homePageView

urlpattterns = [

    path('', homePageView, name = 'home')

]