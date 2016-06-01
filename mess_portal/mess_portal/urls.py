from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^mess_menu/', include('mess_menu.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]
