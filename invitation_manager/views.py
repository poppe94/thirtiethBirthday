from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
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


def link_identifier_auth(request, link_identifier):
    try:
        guest = Guest.objects.get(link_identifier=link_identifier)
    except Guest.DoesNotExist:
        return HttpResponseForbidden()

    login(request, guest.user)

    return redirect("invitation")


@login_required(redirect_field_name=None)
def invitation(request):
    try:
        content = Content.objects.latest('id')
    except Content.DoesNotExist:
        content = None

    context = {
        "content": content,
    }

    return render(request, "invitation_manager/register.html", context=context)


"""

todo:
  - implement resumee template

  - vertical carousel ? 
    - https://stackoverflow.com/questions/70922609/vertical-carousel-in-bootstrap-5
    - https://stackoverflow.com/questions/31561800/scroll-image-continuously-in-html-bootstrap
  - new mode for location address coords? etc, to not make it public on github

  - display invite link on changelist 

"""
