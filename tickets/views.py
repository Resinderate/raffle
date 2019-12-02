from django.views.generic import TemplateView

from tickets.models import Session


class SessionView(TemplateView):
    template_name = "tickets/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_session = Session.objects.latest("created_at")
        tickets = latest_session.tickets.all()
        context["tickets"] = tickets
        return context
