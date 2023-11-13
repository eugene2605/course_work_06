from django.urls import path
from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    ClientCreateView, ClientListView, ClientDeleteView, home, mailing_toggle_activity

app_name = MailingsConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('list_mailing', MailingListView.as_view(), name='list_mailing'),
    path('view_mailing/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('edit_mailing/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('list_client/', ClientListView.as_view(), name='list_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('mailing_activity/<int:pk>/', mailing_toggle_activity, name='mailing_toggle_activity'),
]