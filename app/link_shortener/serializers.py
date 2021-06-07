from rest_framework import serializers, status
from link_shortener.models import LinkShortener


def validate_full_link(full_link):
    return LinkShortener.objects.filter(full_link=full_link).exists()


def error_msg():
    return 'The provided link exists'


class LinkShortenerSerializer(serializers.ModelSerializer):
    """Serializer for LinkShortener objects"""

    class Meta:
        model = LinkShortener
        fields = ('id', 'full_link', 'hash')
        read_only_fields = ('id', 'hash',)

    def create(self, validated_data):
        """Validate if a provided link exist"""
        full_link = validated_data.get('full_link')

        if validate_full_link(full_link):
            raise serializers.ValidationError(
                    error_msg(), code=status.HTTP_400_BAD_REQUEST)
        return LinkShortener.objects.create(**validated_data)

    def update(self, instance, validated_data):
        full_link = validated_data.get('full_link')
        if validate_full_link(full_link):
            raise serializers.ValidationError(
                    error_msg(), code=status.HTTP_400_BAD_REQUEST)

        instance.full_link = full_link
        instance.save()
        return instance
