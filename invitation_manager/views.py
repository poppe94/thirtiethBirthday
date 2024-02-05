import datetime

from django.forms import modelformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django_downloadview import ObjectDownloadView

from invitation_manager.forms import EntourageForm, GuestInfoForm
from invitation_manager.models.guest import Entourage, Guest
from invitation_manager.models.content import Content, ImageFile


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
    if not guest.visited_on:
        guest.visited_on = datetime.datetime.now()
        guest.save()

    return redirect("invitation")


@login_required(redirect_field_name=None)
def invitation(request):
    try:
        content = Content.objects.latest('id')
    except Content.DoesNotExist:
        content = None

    guest_object = Guest.objects.get(user=request.user)
    EntourageFormSet = modelformset_factory(Entourage, form=EntourageForm, min_num=1, extra=0, max_num=3)

    context = {
        "content": content,
        "guest": guest_object,
        "info_form": GuestInfoForm(instance=guest_object),
        "entourage_formset": EntourageFormSet(queryset=guest_object.entourage_set.all())
    }

    return render(request, "invitation_manager/register.html", context=context)


@login_required(redirect_field_name=None)
def info_form_handler(request):
    guest_obj = Guest.objects.get(user=request.user)
    EntourageFormSet = modelformset_factory(Entourage, form=EntourageForm, min_num=1, extra=0, max_num=3)
    guest_info_form = GuestInfoForm(instance=guest_obj)
    entourage_formset = EntourageFormSet(queryset=guest_obj.entourage_set.all())

    if request.method == "POST":
        guest_info_form = GuestInfoForm(request.POST, instance=guest_obj)
        entourage_formset = EntourageFormSet(request.POST)

        if "cancel" in request.POST:
            guest_info_form = GuestInfoForm(instance=guest_obj)
            entourage_formset = EntourageFormSet()

            if request.POST.get("cancel") == "True":
                guest_obj.cancelled = True
                guest_obj.confirmed = False
                guest_obj.cancelled_on = datetime.datetime.now()
                guest_obj.save()
            else:
                guest_obj.cancelled = False
                guest_obj.confirmed = False
                guest_obj.cancelled_on = None
                guest_obj.save()

        elif guest_info_form.is_valid() and entourage_formset.is_valid():
            guest_obj = guest_info_form.save(commit=False)
            if not guest_obj.confirmed:
                guest_obj.confirmed_on = datetime.datetime.now()
            guest_obj.confirmed = True
            guest_obj.save()

            entourage_instances = entourage_formset.save(commit=False)
            for entourage in entourage_instances:
                entourage.guest = guest_obj
                entourage.save()

    context = {
        "guest": guest_obj,
        "info_form": guest_info_form,
        "entourage_formset": entourage_formset
    }

    return render(request, "invitation_manager/info_form.html", context=context)


"""

todo:
  - new model for location address coords? etc, to not make it public on github

  - display invite link on changelist 

"""
