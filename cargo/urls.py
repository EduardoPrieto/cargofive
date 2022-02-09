from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.new_contract, name='new_contract'),
    path('contracts', views.contracts, name='contracts'),
    path('contract/<int:contract_id>', views.contract, name='contract'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)