from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("submit-lead/", views.submit_lead, name="submit_lead"),
    path("contact/", views.contact, name="contact"),
    path("catalog/", views.catalog, name="catalog"),
]
