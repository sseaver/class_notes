from rest_framework import serializers

from menu.models import Special


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Special
