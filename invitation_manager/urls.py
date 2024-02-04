from django.urls import path, re_path

from . import constants, views

urlpatterns = [
    path("register/", views.invitation, name="invitation"),
    re_path(f"auth/(?P<link_identifier>[0-9a-fA-F]{{{constants.LINK_IDENTIFIER_LENGTH}}})/",
            views.link_identifier_auth, name="link-identifier-auth"),
    path("htmx/info-form/", views.info_form_handler, name="info-form-handler"),
    path("content-image/<int:pk>/", views.image_file_view, name="image-file-view"),
]
