import io

from car.models import Car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)

    if serializer.is_valid():
        return JSONRenderer().render(car)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)

    if serializer.is_valid():
        return serializer.validated_data
