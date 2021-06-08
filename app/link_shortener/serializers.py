from rest_framework import serializers, status
from link_shortener.models import LinkShortener


def validate_full_link(validated_data):
    ERROR_MSG = 'The provided link exists'
    full_link = validated_data.get('full_link')

    if LinkShortener.objects.filter(full_link=full_link.lower()).exists():
        raise serializers.ValidationError(
                ERROR_MSG, code=status.HTTP_400_BAD_REQUEST)

    return full_link


class LinkShortenerSerializer(serializers.ModelSerializer):
    """Serializer for LinkShortener objects"""

    class Meta:
        model = LinkShortener
        fields = ('id', 'full_link', 'hash')
        read_only_fields = ('id', 'hash',)

    def create(self, validated_data):
        """Validate if a provided link exist"""
        validate_full_link(validated_data)
        return LinkShortener.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Validate if a provided link exist"""
        instance.full_link = validate_full_link(validated_data)
        instance.save()
        return instance
