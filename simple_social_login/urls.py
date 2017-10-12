from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', include('users.urls'))
]

handler404 = 'simple_social_login.views.handle_page_not_found'
