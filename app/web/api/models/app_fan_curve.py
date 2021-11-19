# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.web.api.models.base_model_ import Model
from app.web.api.models.app_fan_curve_all_of import AppFanCurveAllOf
from app.web.api.models.app_fan_curve_base import AppFanCurveBase
from app.web.api.models.app_fan_curve_series_point import AppFanCurveSeriesPoint
from app.web.api import util

from app.web.api.models.app_fan_curve_all_of import AppFanCurveAllOf  # noqa: E501
from app.web.api.models.app_fan_curve_base import AppFanCurveBase  # noqa: E501
from app.web.api.models.app_fan_curve_series_point import AppFanCurveSeriesPoint  # noqa: E501

class AppFanCurve(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, fan_curve_series=None):  # noqa: E501
        """AppFanCurve - a model defined in OpenAPI

        :param id: The id of this AppFanCurve.  # noqa: E501
        :type id: str
        :param name: The name of this AppFanCurve.  # noqa: E501
        :type name: str
        :param fan_curve_series: The fan_curve_series of this AppFanCurve.  # noqa: E501
        :type fan_curve_series: list[AppFanCurveSeriesPoint]
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'fan_curve_series': list[AppFanCurveSeriesPoint]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'fan_curve_series': 'fanCurveSeries'
        }

        self._id = id
        self._name = name
        self._fan_curve_series = fan_curve_series

    @classmethod
    def from_dict(cls, dikt) -> 'AppFanCurve':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppFanCurve of this AppFanCurve.  # noqa: E501
        :rtype: AppFanCurve
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AppFanCurve.

        Id of fan curve  # noqa: E501

        :return: The id of this AppFanCurve.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppFanCurve.

        Id of fan curve  # noqa: E501

        :param id: The id of this AppFanCurve.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AppFanCurve.

        Name of the fan curve  # noqa: E501

        :return: The name of this AppFanCurve.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppFanCurve.

        Name of the fan curve  # noqa: E501

        :param name: The name of this AppFanCurve.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def fan_curve_series(self):
        """Gets the fan_curve_series of this AppFanCurve.

        Array comprised of all fan series points  # noqa: E501

        :return: The fan_curve_series of this AppFanCurve.
        :rtype: list[AppFanCurveSeriesPoint]
        """
        return self._fan_curve_series

    @fan_curve_series.setter
    def fan_curve_series(self, fan_curve_series):
        """Sets the fan_curve_series of this AppFanCurve.

        Array comprised of all fan series points  # noqa: E501

        :param fan_curve_series: The fan_curve_series of this AppFanCurve.
        :type fan_curve_series: list[AppFanCurveSeriesPoint]
        """
        if fan_curve_series is None:
            raise ValueError("Invalid value for `fan_curve_series`, must not be `None`")  # noqa: E501
        if fan_curve_series is not None and len(fan_curve_series) > 10:
            raise ValueError("Invalid value for `fan_curve_series`, number of items must be less than or equal to `10`")  # noqa: E501
        if fan_curve_series is not None and len(fan_curve_series) < 1:
            raise ValueError("Invalid value for `fan_curve_series`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._fan_curve_series = fan_curve_series