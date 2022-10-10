from django.views import generic
from advertisements_app.models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
