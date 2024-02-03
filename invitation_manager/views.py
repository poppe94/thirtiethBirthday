from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django_downloadview import ObjectDownloadView

from invitation_manager.models.guest import Guest
from invitation_manager.models.content import Content, ImageFile


# Create your views here.

image_file_view = login_required(
    ObjectDownloadView.as_view(model=ImageFile, file_field='image'),
    redirect_field_name=None
)


def index(request, link_identifier):
    try:
        guest = Guest.objects.get(link_identifier=link_identifier)
    except Guest.DoesNotExist:
        # todo redirect to fail state or render feil page
        return render(request, "invitation_manager/link_id_test.html", context={})

    login(request, guest.user)
    try:
        content = Content.objects.latest('id')
    except Content.DoesNotExist:
        content = None

    context = {
        "link_identifier": link_identifier,
        "content": content,
    }

    return render(request, "invitation_manager/link_id_test.html", context=context)


@login_required(redirect_field_name=None)
def test_auth(request):
    return render(request, "invitation_manager/link_id_test.html", context={"auth": True})



"""

todo:
  - implement resume template

  - vertical carousel ? 
    - https://stackoverflow.com/questions/70922609/vertical-carousel-in-bootstrap-5
    - https://stackoverflow.com/questions/31561800/scroll-image-continuously-in-html-bootstrap
  - new mode for location address coords? etc, to not make it public on github
  - field for guest to enter some notes
  - admin should set user automatically
  - display invite link on changelist 

"""
