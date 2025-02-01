from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateGetSensorView, SensorView, UpdateMeasurement

urlpatterns = [
    path('sensors/', CreateGetSensorView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', UpdateMeasurement.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
