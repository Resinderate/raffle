from rest_framework.views import APIView
from rest_framework.response import Response

from reports.models import Section
from reports.serializers import SectionSerializer


class SectionsView(APIView):

    def get(self, request, format=None):

        sections = Section.objects.all().order_by("order").prefetch_related("quotes")

        data = {}
        data["items"] = SectionSerializer(sections, many=True).data

        r = Response(data=data)
        r["Access-Control-Allow-Origin"] = "*"
        return r
