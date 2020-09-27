from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

@api_view(['GET'])
def getlist(request):
    if request.method == 'GET':
        users = User.objects.values('id', 'name', 'age').distinct()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getlistpic(request):
    id = request.GET['id']
    if id is not None:
        users = User.objects.filter(id=id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(str('请传id'))