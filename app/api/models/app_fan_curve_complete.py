# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.api.models.base_model_ import Model
from app.api.models.app_fan_curve_complete_one_of import AppFanCurveCompleteOneOf
from app.api.models.app_fan_curve_series_point import AppFanCurveSeriesPoint
from app.api.models.app_fan_curve_update import AppFanCurveUpdate
from app.api import util

from app.api.models.app_fan_curve_complete_one_of import AppFanCurveCompleteOneOf  # noqa: E501
from app.api.models.app_fan_curve_series_point import AppFanCurveSeriesPoint  # noqa: E501
from app.api.models.app_fan_curve_update import AppFanCurveUpdate  # noqa: E501

class AppFanCurveComplete(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, last_time_changed=None, name=None, fan_curve_series=None):  # noqa: E501
        """AppFanCurveComplete - a model defined in OpenAPI

        :param id: The id of this AppFanCurveComplete.  # noqa: E501
        :type id: str
        :param last_time_changed: The last_time_changed of this AppFanCurveComplete.  # noqa: E501
        :type last_time_changed: datetime
        :param name: The name of this AppFanCurveComplete.  # noqa: E501
        :type name: str
        :param fan_curve_series: The fan_curve_series of this AppFanCurveComplete.  # noqa: E501
        :type fan_curve_series: list[AppFanCurveSeriesPoint]
        """
        self.openapi_types = {
            'id': str,
            'last_time_changed': datetime,
            'name': str,
            'fan_curve_series': list[AppFanCurveSeriesPoint]
        }

        self.attribute_map = {
            'id': 'id',
            'last_time_changed': 'lastTimeChanged',
            'name': 'name',
            'fan_curve_series': 'fanCurveSeries'
        }

        self._id = id
        self._last_time_changed = last_time_changed
        self._name = name
        self._fan_curve_series = fan_curve_series

    @classmethod
    def from_dict(cls, dikt) -> 'AppFanCurveComplete':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppFanCurveComplete of this AppFanCurveComplete.  # noqa: E501
        :rtype: AppFanCurveComplete
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AppFanCurveComplete.

        Id of fan curve  # noqa: E501

        :return: The id of this AppFanCurveComplete.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppFanCurveComplete.

        Id of fan curve  # noqa: E501

        :param id: The id of this AppFanCurveComplete.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def last_time_changed(self):
        """Gets the last_time_changed of this AppFanCurveComplete.

        Last time fan curve was updated (used for optimistic locking)  # noqa: E501

        :return: The last_time_changed of this AppFanCurveComplete.
        :rtype: datetime
        """
        return self._last_time_changed

    @last_time_changed.setter
    def last_time_changed(self, last_time_changed):
        """Sets the last_time_changed of this AppFanCurveComplete.

        Last time fan curve was updated (used for optimistic locking)  # noqa: E501

        :param last_time_changed: The last_time_changed of this AppFanCurveComplete.
        :type last_time_changed: datetime
        """
        if last_time_changed is None:
            raise ValueError("Invalid value for `last_time_changed`, must not be `None`")  # noqa: E501

        self._last_time_changed = last_time_changed

    @property
    def name(self):
        """Gets the name of this AppFanCurveComplete.

        Name of the fan curve  # noqa: E501

        :return: The name of this AppFanCurveComplete.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppFanCurveComplete.

        Name of the fan curve  # noqa: E501

        :param name: The name of this AppFanCurveComplete.
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
        """Gets the fan_curve_series of this AppFanCurveComplete.

        Array comprised of all fan series points  # noqa: E501

        :return: The fan_curve_series of this AppFanCurveComplete.
        :rtype: list[AppFanCurveSeriesPoint]
        """
        return self._fan_curve_series

    @fan_curve_series.setter
    def fan_curve_series(self, fan_curve_series):
        """Sets the fan_curve_series of this AppFanCurveComplete.

        Array comprised of all fan series points  # noqa: E501

        :param fan_curve_series: The fan_curve_series of this AppFanCurveComplete.
        :type fan_curve_series: list[AppFanCurveSeriesPoint]
        """
        if fan_curve_series is None:
            raise ValueError("Invalid value for `fan_curve_series`, must not be `None`")  # noqa: E501
        if fan_curve_series is not None and len(fan_curve_series) > 10:
            raise ValueError("Invalid value for `fan_curve_series`, number of items must be less than or equal to `10`")  # noqa: E501
        if fan_curve_series is not None and len(fan_curve_series) < 1:
            raise ValueError("Invalid value for `fan_curve_series`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._fan_curve_series = fan_curve_series
