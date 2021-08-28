from reports.models import Quote, Section, Tag
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ["name", "quotes", "id"]

    quotes = SerializerMethodField()

    def get_quotes(self, section):
        return QuoteSerializer(
            section.quotes.all().order_by("-is_positive", "order"),
            many=True,
        ).data


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "id"]


class QuoteSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Quote
        fields = ["content", "is_positive", "id", "tags"]
