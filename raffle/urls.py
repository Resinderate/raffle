from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path

from reports.views import QuoteList, QuoteBeta
from tickets.views import SessionView, ClassListView, ClassSessionListView
from tickets.views_api import TicketsView

urlpatterns = [
    path('raffle/api/tickets/', TicketsView.as_view()),
    path('admin/', admin.site.urls),
    path('raffle/', ClassListView.as_view()),
    path('raffle/<slug:class>/', ClassSessionListView.as_view()),
    path('raffle/<slug:class>/<slug:session>/', SessionView.as_view()),
    path('', RedirectView.as_view(url='/raffle/')),
    path('reports/', QuoteList.as_view()),
    path('reports/beta/', QuoteBeta.as_view()),
]
