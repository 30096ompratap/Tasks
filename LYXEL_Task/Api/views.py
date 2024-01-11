from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import YourModel
from .serializers import YourModelSerializer

@api_view(['GET'])
def insert_data(request):
    timestamp = request.GET.get('timestamp')
    value = request.GET.get('value')
    YourModel.objects.create(timestamp=timestamp, value=value)
    return Response({'message': 'Data inserted successfully'})

@api_view(['GET'])
def graph_data(request):
    data = YourModel.objects.values('timestamp').annotate(value=Sum('value')).order_by('timestamp')
    serialized_data = YourModelSerializer(data, many=True).data
    return Response({'data': serialized_data})

