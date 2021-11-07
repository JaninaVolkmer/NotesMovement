from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Entry
# Create your views here.


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class EntryListView(LockedView, ListView):
    model = Entry
    # return all entries ordered by their primary key + ascending order
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    # define what model field should be displayed in the form
    fields = ["title", "notes"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new workout was created!"


"""
EntryUpdateView:
define where user gets redirected after submitting the form
.get_success_url() returns value of success_url by default
:provide entry.id as keyword argument: stay on entry detail page after editing
:reverse_lazy: refer to URLs by name as in templates
"""


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    # define what model field should be displayed in the form
    fields = ["title", "notes"]
    success_message = "Your workout has been updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )


"""
EntryDeleteView:
need extra method because DeleteView class is
no ancestor of FormView
:Skip SuccessMessageMixin as param
"""


class EntryDeleteView(LockedView, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your workout was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
