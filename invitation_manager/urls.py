from django.urls import path, re_path

from . import constants, views

urlpatterns = [
    re_path(f"(?P<link_identifier>[0-9a-fA-F]{{{constants.LINK_IDENTIFIER_LENGTH}}})/", views.index, name="index"),
    path("info/", views.test_auth, name="test")
]
