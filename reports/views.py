from django.views.generic import ListView

from reports.models import Grade, Quote


class GradeList(ListView):
    template_name = "reports/class_list.html"
    context_object_name = 'grades'
    model = Grade


class QuoteList(ListView):
    template_name = "reports/quote_list.html"
    context_object_name = 'quotes'

    def get_queryset(self):
        grade_id = self.kwargs["grade_id"]
        quotes = Quote.objects.filter(grade_id=grade_id)
        print("quotes:", quotes)
        return quotes

    # Can add in extra stuff later.
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("context:", context)
    #     return context
