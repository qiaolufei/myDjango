from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

@api_view(['GET'])
def getlist(request):  # 获取全部数据
    if request.method == 'GET':
        users = User.objects.values('id', 'name', 'age').distinct()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getlistpic(request):  # 根据id查找单条数据
    id = request.GET['id']
    if id is not None:
        users = User.objects.filter(id=id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(str('请传id'))

@api_view(['POST'])
def addUser(request):  # 添加数据
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
       ser.save()
       return Response(ser.data)
    return Response(ser.errors)

@api_view(['GET'])
def deleteUser(request):  # 根据id添加删除
    id = request.GET['id']
    if id is not None:
        if User.objects.filter(id=id):
            User.objects.get(id=id).delete()
            return Response(str('success'))
        else:
            return Response(str('没有此id'))
    else:
        return Response(str('请传id'))

@api_view(['POST'])
def updateUser(request):  # 根据id修改数据
    if User.objects.filter(id=request.data['id']):
        user = User.objects.get(id=request.data['id'])
        ser = UserSerializer(instance=user, data=request.data)  # 注意指定参数
        if ser.is_valid():
            ser.save()
            return Response(str('success'))
        return Response(ser.errors)
    return Response(str('没有此id'))
