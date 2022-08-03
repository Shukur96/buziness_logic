from django.urls import path
from . import views

urlpatterns = [
    path('add_to common_list',views.add_to_common_list_views),
    path('add_to_case_list',views.add_to_case_list_views)
]
