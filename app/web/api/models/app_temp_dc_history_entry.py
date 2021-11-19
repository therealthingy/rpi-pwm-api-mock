# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.web.api.models.base_model_ import Model
from app.web.api import util


class AppTempDCHistoryEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, date=None, temp_in_cels=None, fan_dcin_perc=None):  # noqa: E501
        """AppTempDCHistoryEntry - a model defined in OpenAPI

        :param date: The date of this AppTempDCHistoryEntry.  # noqa: E501
        :type date: datetime
        :param temp_in_cels: The temp_in_cels of this AppTempDCHistoryEntry.  # noqa: E501
        :type temp_in_cels: int
        :param fan_dcin_perc: The fan_dcin_perc of this AppTempDCHistoryEntry.  # noqa: E501
        :type fan_dcin_perc: int
        """
        self.openapi_types = {
            'date': datetime,
            'temp_in_cels': int,
            'fan_dcin_perc': int
        }

        self.attribute_map = {
            'date': 'date',
            'temp_in_cels': 'tempInCels',
            'fan_dcin_perc': 'fanDCInPerc'
        }

        self._date = date
        self._temp_in_cels = temp_in_cels
        self._fan_dcin_perc = fan_dcin_perc

    @classmethod
    def from_dict(cls, dikt) -> 'AppTempDCHistoryEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppTempDCHistoryEntry of this AppTempDCHistoryEntry.  # noqa: E501
        :rtype: AppTempDCHistoryEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def date(self):
        """Gets the date of this AppTempDCHistoryEntry.

        Date of this entry  # noqa: E501

        :return: The date of this AppTempDCHistoryEntry.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AppTempDCHistoryEntry.

        Date of this entry  # noqa: E501

        :param date: The date of this AppTempDCHistoryEntry.
        :type date: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def temp_in_cels(self):
        """Gets the temp_in_cels of this AppTempDCHistoryEntry.

        Temperature in percent at the date `date`  # noqa: E501

        :return: The temp_in_cels of this AppTempDCHistoryEntry.
        :rtype: int
        """
        return self._temp_in_cels

    @temp_in_cels.setter
    def temp_in_cels(self, temp_in_cels):
        """Sets the temp_in_cels of this AppTempDCHistoryEntry.

        Temperature in percent at the date `date`  # noqa: E501

        :param temp_in_cels: The temp_in_cels of this AppTempDCHistoryEntry.
        :type temp_in_cels: int
        """
        if temp_in_cels is None:
            raise ValueError("Invalid value for `temp_in_cels`, must not be `None`")  # noqa: E501

        self._temp_in_cels = temp_in_cels

    @property
    def fan_dcin_perc(self):
        """Gets the fan_dcin_perc of this AppTempDCHistoryEntry.

        Fan speed in percent at the date `date`  # noqa: E501

        :return: The fan_dcin_perc of this AppTempDCHistoryEntry.
        :rtype: int
        """
        return self._fan_dcin_perc

    @fan_dcin_perc.setter
    def fan_dcin_perc(self, fan_dcin_perc):
        """Sets the fan_dcin_perc of this AppTempDCHistoryEntry.

        Fan speed in percent at the date `date`  # noqa: E501

        :param fan_dcin_perc: The fan_dcin_perc of this AppTempDCHistoryEntry.
        :type fan_dcin_perc: int
        """
        if fan_dcin_perc is None:
            raise ValueError("Invalid value for `fan_dcin_perc`, must not be `None`")  # noqa: E501
        if fan_dcin_perc is not None and fan_dcin_perc > 100:  # noqa: E501
            raise ValueError("Invalid value for `fan_dcin_perc`, must be a value less than or equal to `100`")  # noqa: E501
        if fan_dcin_perc is not None and fan_dcin_perc < 0:  # noqa: E501
            raise ValueError("Invalid value for `fan_dcin_perc`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fan_dcin_perc = fan_dcin_perc