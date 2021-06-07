from rest_framework import viewsets, status
from link_shortener.models import LinkShortener
from link_shortener import serializers
from django.views import View
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView


class LinkShortenerViewSet(viewsets.ModelViewSet):
    """ Manage links shortener in the database."""
    serializer_class = serializers.LinkShortenerSerializer
    queryset = LinkShortener.objects.all().order_by('-id')

    def get_queryset(self):
        """Retrieve shorted links by full link"""
        full_link = self.request.query_params.get('full_link', False)
        queryset = self.queryset

        if full_link:
            queryset = queryset.filter(full_link=full_link)

        return queryset


class ValidateShortedLink(APIView):
    def get(self, request, hash, *args, **kwargs):
        try:
            return redirect(LinkShortener.objects.get(hash=hash).full_link)
        except LinkShortener.DoesNotExist:
            return Response("The provided shorted link does not exist.",
                            status=status.HTTP_400_BAD_REQUEST)
