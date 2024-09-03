from django.urls import path
from . import views

urlpatterns=[
    path('addresslist/',views.GetUSerAddresses.as_view(),name='user-addresses'),
    path('add/',views.AddAddress.as_view(),name='add-address'),
    path('default/',views.SetDefaultAddress.as_view(),name='default-address'),
    path('delete/',views.DeleteAddress.as_view(),name='delete-address'),
    path('me/',views.GetDefaultAddress.as_view(),name='user-addresses')
]
