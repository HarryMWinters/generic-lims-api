from django.contrib.auth.models import User, Group
from rest_framework import serializers

from RestApi.models import Assay
from django.contrib.auth.models import User


class AssaySerializer(serializers.ModelSerializer):
    """ This is the short _implicit_ way"""
    class Meta:
        model = Assay
        fields = ["record_timestamp", "title", "code", "active"]
        # Equivalent to fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

# This is the long, explicit way...
# class AssaySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     record_timestamp = serializers.DateTimeField(read_only=True)
#     title = serializers.CharField()
#     code = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Assay` instance, given the validated data.
#         """
#         return Assay.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Assay` instance, given the validated data.
#         """
#         instance.record_timestamp = validated_data.get(
#             "record_timestamp", instance.record_timestamp)
#         instance.title = validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.active = validated_data.get("active", instance.active)
#
