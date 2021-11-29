from django.urls import path

from . import views

app_name = "temperatures"


urlpatterns = [
    path("temperatures", views.TemperatureListView.as_view(), name="temperature-list"),
    path(
        "detail-<int:pk>",
        views.TemperatureDetailView.as_view(),
        name="temperature-detail",
    ),
    path("", views.TemperatureCreateView.as_view(), name="temperature-create"),
    path(
        "update-<int:pk>",
        views.TemperatureUpdateView.as_view(),
        name="temperature-update",
    ),
]
