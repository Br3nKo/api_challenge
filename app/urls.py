from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('countries/', views.CountryList.as_view()),
    path('countries/<int:id>/', views.CountryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
