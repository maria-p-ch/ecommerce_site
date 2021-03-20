from rest_framework import serializers

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'shipping_address',
            'shipping_zip_code'
        )
