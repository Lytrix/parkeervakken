import json
import logging

from rest_framework import serializers

from parkeervakken_api.rest import DisplayField
from parkeervakken_api.rest import HALSerializer
from parkeervakken_api.models import Parkeervak


class BaseSerializer(object):

    def href_url(self, path):
        """Prepend scheme and hostname"""
        base_url = '{}://{}'.format(
            self.context['request'].scheme,
            self.context['request'].get_host())
        return base_url + path

    def dict_with_self_href(self, path):
        return {
            "self": {
                "href": self.href_url(path)
            }
        }

    def dict_with__links_self_href_id(self, path, id, id_name):
        return {
            "_links": {
                "self": {
                    "href": self.href_url(path.format(id))
                }
            },
            id_name: id
        }

    def dict_with_count_href(self, count, path):
        return {
            "count": count,
            "href": self.href_url(path)
        }


class ParkeervakSerializer(BaseSerializer, HALSerializer):
    _display = DisplayField()

    filter_fields = ('id')

    class Meta(object):
        model = Parkeervak
        fields = '__all__'