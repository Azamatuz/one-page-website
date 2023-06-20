from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from one_page_app.views import home

app_name = 'one_page_app'

urlpatterns = [
    path('', home, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)