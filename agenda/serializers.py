from rest_framework import serializers

from . import models


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.Entry
