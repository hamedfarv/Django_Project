## we are going to map url to view functions
from django.urls import path
from . import views
#from storefront import playground

# URL conf module
urlpatterns = [
path("hello/",views.say_hello) ,
path("hello_html/",views.say_hello_HTML)

]
