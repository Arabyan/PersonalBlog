
from django.conf.urls import url
from django.contrib import admin
from posts import views
import sitepages.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name="home"),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name="post_detail"),
    url(r'^about/', sitepages.views.about,name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
