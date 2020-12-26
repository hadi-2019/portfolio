from django.urls import path
from .views import index, detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="home-page"),
    path('detail/<int:id>/', detail, name="detail-page"),
] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
