from django.urls import path
from .views import contact_list, add_contact, delete_contact, send_contact_email

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/add/', add_contact, name='add_contact'),
    path('contacts/delete/<int:contact_id>/', delete_contact, name='delete_contact'),
    path('contacts/send_email/<int:contact_id>/', send_contact_email, name='send_contact_email'),
]
