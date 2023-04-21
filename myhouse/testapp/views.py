from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
import logging

from testapp.models import Entity, Property
from testapp.serializers import EntitySerializer, PropertySerializer


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(modified_by=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Метод который проверяет входящий json на POST и дает возможность менять название поля
        """
        if 'data[value]' in request.data:
            request.data['value'] = request.data['data[value]']
            request.data.pop('data[value]')
        else:
            pass
        valid_ser = self.serializer_class(data=request.data)
        if valid_ser.is_valid():
            valid_ser.save(modified_by=self.request.user) # сохраняет USER id foreign_key В БД не явно
            return Response(valid_ser.data)
        return Response('False')



    # def get_queryset(self):
    #     queryset = Entity.objects.all()
    #     main_list = []
    #     for obj in queryset:
    #         obj_dict = {}
    #         que = obj.properties.all()
    #         for value in que.values():
    #             obj_dict['id'] = value['id']
    #             obj_dict[value['key']] = value['value']
    #
    #
    #         #print(obj_dict)
    #         obj.properties.set
    #         #print(obj.properties)
    #     return(queryset)







