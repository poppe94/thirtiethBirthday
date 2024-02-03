from django.views.generic import TemplateView

custom_page_not_found_view = None

custom_error_view = None

permission_denied_view = TemplateView.as_view(template_name='403.html')  # todo this error does not really work??

custom_bad_request_view = None
