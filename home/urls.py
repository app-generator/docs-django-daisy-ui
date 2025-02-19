from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/hello", views.hello, name="hello"),
    # tools
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]
