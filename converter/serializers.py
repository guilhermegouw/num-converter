from rest_framework import serializers


class NumberToEnglishRequestSerializer(serializers.Serializer):
    number = serializers.CharField(required=True, allow_blank=False, max_length=12)
