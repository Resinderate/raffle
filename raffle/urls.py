from django.contrib import admin
from django.urls import path

from tickets.views import SessionView, ClassListView, ClassSessionListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('raffle/', ClassListView.as_view()),
    path('raffle/<slug:class>/', ClassSessionListView.as_view()),
    path('raffle/<slug:class_slug>/<slug:session_slug>/', SessionView.as_view()),
]
