from rest_framework import serializers
from .models import *

class BookSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = ['title', 'owner']
        read_only_fields = ['owner']