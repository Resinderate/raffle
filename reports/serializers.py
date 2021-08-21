from reports.models import Quote, Section
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ["name", "quotes"]

    quotes = SerializerMethodField()

    def get_quotes(self, section):
        return QuoteSerializer(
            section.quotes.all().order_by("-is_positive", "order"),
            many=True,
        ).data


class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = ["content", "is_positive"]
