from django.views.generic import TemplateView, ListView

from tickets.models import Session, Class


class ClassListView(ListView):
    template_name = "tickets/class_list.html"
    context_object_name = 'classes'
    model = Class


class ClassSessionListView(ListView):
    template_name = "tickets/session_list.html"
    context_object_name = 'sessions'

    def get_queryset(self):
        slug = self.kwargs["class"]
        print("Slug:", slug)
        return Class.objects.get(slug=slug).sessions.all()


class SessionView(TemplateView):
    template_name = "tickets/session_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # all_players_from_class = 
        # latest_session = Session.objects.latest("created_at")
        # tickets = latest_session.tickets.all()
        # context["tickets"] = tickets
        return context
