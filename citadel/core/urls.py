from django.urls import path
from .views import MaxProfitView

urlpatterns = [
    path('max_profit/', MaxProfitView.as_view(), name='max_profit'),
]
