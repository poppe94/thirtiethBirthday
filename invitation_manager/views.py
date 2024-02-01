from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from invitation_manager.models import Guest


# Create your views here.


def index(request, link_identifier):
    try:
        guest = Guest.objects.get(link_identifier=link_identifier)
    except Guest.DoesNotExist:
        return render(request, "link_id_test.html", context={})

    login(request, guest.user)

    return render(request, "link_id_test.html", context={"link_identifier": link_identifier})


@login_required(redirect_field_name=None)
def test_auth(request):
    return render(request, "link_id_test.html", context={"auth": True})
