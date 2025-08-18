
from  django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('post_details/<int:post_id>', views.post_details, name='post_details')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
