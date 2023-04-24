from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Property, Entity



# class PropertySerializer(serializers.ModelSerializer):
#     property_list = serializers.SerializerMethodField()


#     class Meta:
#         model = Property
#         fields = ('key', 'value')

        


class EntitySerializer(serializers.ModelSerializer):

    value = serializers.IntegerField()
    #properties = PropertySerializer(read_only=True, many=True)
    properties = serializers.SerializerMethodField(read_only=True)

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

#     class Meta:
#        model = Entity
#        fields = ("data[value]", 'properties')

#        extra_kwargs = {
#            "data[value]": {"source": "value"}
#        }



