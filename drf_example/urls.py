"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from test_app.views import (SnippetDetail, SnippetList, SnippetListMixin,
                            UserList, UserDetail, SnippetDetailMixin,
                            SnippetHighlight, UserViewSet, SnippetViewSet)

router = routers.DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]


# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url('api-auth/', include('rest_framework.urls',
#         namespace='rest_framework')),
#     url(r'^admin/', admin.site.urls),
#     url('snippets/$', SnippetListMixin.as_view(), name='snippet-list'),
#     url('snippet/(?P<pk>\d+)/$', SnippetDetailMixin.as_view(),
#         name='snippet-detail'),
#     url('html/(?P<pk>\d+)/$', SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     url('users/$', UserList.as_view(), name='user-list'),
#     url('user/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
# ]
