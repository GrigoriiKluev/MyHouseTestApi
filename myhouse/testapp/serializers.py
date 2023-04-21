from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Property, Entity



class PropertySerializer(serializers.ModelSerializer):
    property_list = serializers.SerializerMethodField()


    class Meta:
        model = Property
        fields = ('key', 'value')


    # def to_representation(self, instance):
    #     data = super().to_representation(instance=instance)
    #     new_dict = {}
    #     new_list = []
    #     for value in data.values():
    #         new_list.append(value)
    #     new_dict[new_list[0]] = new_list[1]
    #     return new_dict


class EntitySerializer(serializers.ModelSerializer):

    value = serializers.IntegerField()
    #properties = PropertySerializer(read_only=True, many=True)
    properties = serializers.SerializerMethodField()

    def get_properties(self, instance): # Метод поля который переопределяет вывод связанных моделей many_to_many
        correct_dict = {}
        que = instance.properties.get_queryset()
        for value in que.values():
            #correct_dict['id'] = value['id']
            correct_dict[value['key']] = value['value']
        return correct_dict


    class Meta:
       model = Entity
       fields = ('value', 'properties')

   # def to_internal_value(self, data):
   #    if 'data[value]' in data.keys():
   #       data["value"] = data['data[value]']
   #       data.pop('data[value]')
   #    else:
   #       pass
   #    return data


   # def create(self, validated_data):
   #    return Entity.objects.create(**validated_data)



