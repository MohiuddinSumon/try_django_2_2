"""Try_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from .views import (
    about,
    home_page,
    contact,
    user
)
from blog.views import (
    blog_post_create_view,
    blog_post_create_model_view,
)

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('about/',about),
    path('gql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('contact/', contact),
    path('user/', user),
    path('example/', about),
    path('blog-new', blog_post_create_view),
    path('blog-new-model', blog_post_create_model_view),
    path('blog/', include('blog.urls')),


    url(r'^keycloak/', include('django_keycloak.urls')),

]


