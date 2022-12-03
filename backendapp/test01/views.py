from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Test01
from .serializers import TestDataSerializer


@api_view(['GET'])
def getTestDatas(request):
    datas = Test01.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

# Create your views here.

@api_view(['POST'])
def postMember(request):
    reqData = request.data
    serializer = TestDataSerializer(data=reqData)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)