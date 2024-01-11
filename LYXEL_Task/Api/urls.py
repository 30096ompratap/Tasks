from django.urls import path
from .views import insert_data, graph_data

urlpatterns = [
    path('api/insert/', insert_data, name='insert_data'),
    path('api/graph/', graph_data, name='graph_data'),
]
