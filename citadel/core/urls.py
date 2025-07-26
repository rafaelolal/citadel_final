from django.urls import path
<<<<<<< HEAD
from .views import MaxProfitView

urlpatterns = [
    path('max_profit/', MaxProfitView.as_view(), name='max_profit'),
=======
from .views import MaxProfitView, LLMView

urlpatterns = [
    path('max_profit/', MaxProfitView.as_view(), name='max_profit'),
    path('llm/', LLMView.as_view(), name='llm'),
>>>>>>> c3d67408cda330c6b1850ebe0fb3eed37120c0c8
]
