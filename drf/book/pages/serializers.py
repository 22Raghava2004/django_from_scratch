from rest_framework import serializers
from .models import Pages 

class page_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields='__all__'
        extra_kwargs={
            'author':{'read_only':True}
        }
