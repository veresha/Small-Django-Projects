from django.views import generic
from advertisements_app.models import Advertisement
from django.shortcuts import render


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get_object(self, queryset=None):
        Advertisement.views_plus()


# class AdvCount(generic.View):
#     count = 1
#
#     def get(self, request):
#         AdvCount.count += 1
#         return render(
#          request=request, template_name='advertisements_app/advertisement_detail',
#          context={'views_count': AdvCount.count}
#         )
