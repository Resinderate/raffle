from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from tickets.models import Player, Session, Ticket


class TicketsView(APIView):
    # Need some auth.

    def post(self, request, format=None):
        user_slug = request.data.get("user")
        session_slug = request.data.get("session")
        quantity = request.data.get("quantity")

        try:
            quantity = int(quantity)
        except ValueError:
            raise ValidationError({"quantity": "Must be an int"})

        if quantity < 1:
            raise ValidationError({"quantity": "Can't be less than 1"})

        player = Player.objects.get(slug=user_slug)
        session = Session.objects.get(slug=session_slug)
        tickets = [
            Ticket(player=player, session=session)
            for _ in range(quantity)
        ]
        Ticket.objects.bulk_create(tickets)

        return Response(f"Created {quantity} tickets!")
