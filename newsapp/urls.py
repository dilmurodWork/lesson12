from django.urls import path

from newsapp.views import NewsView, tagged


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<slug:slug>/', tagged, name="tagged"),
]