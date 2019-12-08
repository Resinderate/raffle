import random

from django.views.generic import ListView, DetailView

from tickets.models import Session, Class


class ClassListView(ListView):
    template_name = "tickets/class_list.html"
    context_object_name = 'classes'
    model = Class


class ClassSessionListView(ListView):
    template_name = "tickets/session_list.html"
    context_object_name = 'sessions'

    def get_queryset(self):
        class_slug = self.kwargs["class"]
        self.class_ = Class.objects.get(slug=class_slug)
        return self.class_.sessions.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["class"] = self.class_
        return context


class SessionView(DetailView):
    template_name = "tickets/session_detail.html"
    context_object_name = "session"
    model = Session

    def get_queryset(self):
        class_slug = self.kwargs["class"]
        self.class_ = Class.objects.get(slug=class_slug)
        return self.class_.sessions.all()

    def get_object(self, queryset=None):
        qs = self.get_queryset()
        session_slug = self.kwargs["session"]
        self.session = qs.get(slug=session_slug)
        return self.session

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_players_from_class = self.class_.players.all()
        all_tickets_for_session = self.session.tickets.all()
        ticket_counts = {player.id: {"name": player.name, "count": 0} for player in all_players_from_class}
        for ticket in all_tickets_for_session:
            ticket_counts[ticket.player_id]["count"] += 1

        rankings = sorted(ticket_counts.values(), key=lambda x: x["count"], reverse=True)

        # Find the positions, taking joint places into account.
        ranks = [r["count"] for r in rankings]
        positions = [ranks.index(r) + 1 for r in ranks]
        for i, p in enumerate(positions):
            rankings[i]["position"] = p

        context["rankings"] = rankings

        draw_a_name = bool(self.request.GET.get("draw", False))

        draw_available = len(all_tickets_for_session) > 0
        context["draw_available"] = draw_available
        if not draw_available:
            # Can't draw a name if it's not available
            draw_a_name = False

        if draw_a_name:
            tickets = [ticket.player.name for ticket in all_tickets_for_session]
            winner = random.choice(tickets)
            context["winner"] = winner

        return context
