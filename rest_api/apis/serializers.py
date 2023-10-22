
# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import RestModel
 
# Create a model serializer
class RestSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = RestModel
        fields = ('title', 'description')