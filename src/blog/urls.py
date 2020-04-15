from django.urls import path

from .views import HomeView, EntryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>/', EntryDetailView.as_view(), name="entry_detail"),
]
