from typing import Any

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Advert
from .serializers import AdvertSerializer


class AdvertListApiView(ListAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all().select_related("city", "category")


class AdvertRetrieveApiView(RetrieveAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all().select_related("city", "category")

    def get_object(self) -> Any:
        instance = super().get_object()
        instance.views += 1
        instance.save()
        return instance
