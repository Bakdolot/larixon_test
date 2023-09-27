from django.urls import path

from .views import AdvertListApiView, AdvertRetrieveApiView

urlpatterns = [
    path("advert-list/", AdvertListApiView.as_view()),
    path("advert/<int:pk>/", AdvertRetrieveApiView.as_view()),
]
