from rest_framework import serializers
from license_server.models import TokenErtel


class TokenErtelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenErtel
        fields = \
            [
                'id',
                'token',
                'start_date',
                'counterparty',
                'end_date',
                'tech_support',
                'number_of_activated_devices',
                'number_of_activations',
                'notes',
            ]