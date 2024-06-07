from django.urls import path
from .views import MaxProfitView, LLMView

urlpatterns = [
    path('max_profit/', MaxProfitView.as_view(), name='max_profit'),
    path('llm/', LLMView.as_view(), name='llm'),
]
