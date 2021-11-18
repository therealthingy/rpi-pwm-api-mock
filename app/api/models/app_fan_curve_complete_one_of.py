# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.api.models.base_model_ import Model
from app.api import util


class AppFanCurveCompleteOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None):  # noqa: E501
        """AppFanCurveCompleteOneOf - a model defined in OpenAPI

        :param id: The id of this AppFanCurveCompleteOneOf.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'AppFanCurveCompleteOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppFanCurveComplete_oneOf of this AppFanCurveCompleteOneOf.  # noqa: E501
        :rtype: AppFanCurveCompleteOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AppFanCurveCompleteOneOf.

        Id of fan curve  # noqa: E501

        :return: The id of this AppFanCurveCompleteOneOf.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppFanCurveCompleteOneOf.

        Id of fan curve  # noqa: E501

        :param id: The id of this AppFanCurveCompleteOneOf.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id
