from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class CreateGetSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class UpdateMeasurement(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer

