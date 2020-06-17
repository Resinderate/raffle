from django.views.generic import ListView

from reports.models import Quote


class QuoteList(ListView):
    template_name = "reports/quote_list.html"
    context_object_name = 'quotes'
    model = Quote

    # Can add in extra stuff later.
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("context:", context)
    #     return context
