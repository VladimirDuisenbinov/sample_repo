from django.urls import path
from django.conf.urls import url

from url_short import views

urlpatterns = [
    path('url-shorts/', views.URLShortAPIView.as_view()),
    path('url-shorts/<int:pk>/', views.URLShortListAPIView.as_view()),
    path(r"redirect/<str:short_url>/", views.redirect_view, name="redirect_view"),
]
