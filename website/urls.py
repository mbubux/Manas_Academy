from django.urls import path
from . import views
# import apps.corecode.urls
from apps.corecode.views import IndexView

urlpatterns = [
    path('corecode/', IndexView.as_view(), name='IndexView'),
    path("", views.wb_index , name="wb_index"),
    path("about/", views.wb_about , name="wb_about"),
    path("academics/", views.wb_academics , name="wb_academics"),
    path("admission/", views.wb_admission , name="wb_admission"),
    path("contact/", views.wb_contact , name="wb_contact"),
    path("facilities/", views.wb_facilities , name="wb_facilities"),
    path("faculties/", views.wb_faculties , name="wb_faculties"),
       
]
