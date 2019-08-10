from django.views.generic import TemplateView
from django.views import View
from apps.utils.view.generics import GenericAPIView, APIView
from apps.utils.view.viewsets import ModelViewSet
from apps.schedule.models import Entry
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from apps.utils.pagination import DefaultResultsSetPagination
import rest_framework_filters as filters

# Create your views here.

class SpiderView(TemplateView):
    template_name = 'spider/index.html'


class SiteTypeView(APIView):
    authentication_classes = ()
    permission_classes = ()
    filter_backends = ()

    def get(self, request, *args, **kwargs):
        sites = [{'name': name, 'code': code} for code, name in Entry.site_choices]
        print(sites)
        return Response(sites, status=200)


class EntryModelSerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class EntryFilter(filters.FilterSet):

    class Meta:
        model = Entry
        fields = '__all__'


class EntryViewSet(ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    pagination_class = DefaultResultsSetPagination
    serializer_class = EntryModelSerializer
    queryset = Entry.objects.all()
    filter_class = EntryFilter


