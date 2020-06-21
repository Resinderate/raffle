from django.views.generic import ListView

from reports.models import Section, Quote


class QuoteList(ListView):
    template_name = "reports/quote_list.html"
    context_object_name = "sections"
    model = Quote

    def get_queryset(self):
        self.sections = Section.objects.all().order_by("order").prefetch_related("quotes")
        return self.sections

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = []
        for section in self.sections:
            context["sections"].append({"name": section.name, "quotes": section.quotes.all().order_by("-is_positive", "order")})
        return context


class QuoteBeta(QuoteList):
    template_name = "reports/quote_list_beta.html"
