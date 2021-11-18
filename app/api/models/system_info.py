# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.api.models.base_model_ import Model
from app.api import util


class SystemInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, os_kernel=None, hw_pi_board_rev=None, hw_cpu_hw=None, hw_cpu_rev=None, hw_bootloader_ver=None, exec_user=None):  # noqa: E501
        """SystemInfo - a model defined in OpenAPI

        :param os_kernel: The os_kernel of this SystemInfo.  # noqa: E501
        :type os_kernel: str
        :param hw_pi_board_rev: The hw_pi_board_rev of this SystemInfo.  # noqa: E501
        :type hw_pi_board_rev: str
        :param hw_cpu_hw: The hw_cpu_hw of this SystemInfo.  # noqa: E501
        :type hw_cpu_hw: str
        :param hw_cpu_rev: The hw_cpu_rev of this SystemInfo.  # noqa: E501
        :type hw_cpu_rev: str
        :param hw_bootloader_ver: The hw_bootloader_ver of this SystemInfo.  # noqa: E501
        :type hw_bootloader_ver: str
        :param exec_user: The exec_user of this SystemInfo.  # noqa: E501
        :type exec_user: str
        """
        self.openapi_types = {
            'os_kernel': str,
            'hw_pi_board_rev': str,
            'hw_cpu_hw': str,
            'hw_cpu_rev': str,
            'hw_bootloader_ver': str,
            'exec_user': str
        }

        self.attribute_map = {
            'os_kernel': 'osKernel',
            'hw_pi_board_rev': 'hwPiBoardRev',
            'hw_cpu_hw': 'hwCpuHw',
            'hw_cpu_rev': 'hwCpuRev',
            'hw_bootloader_ver': 'hwBootloaderVer',
            'exec_user': 'execUser'
        }

        self._os_kernel = os_kernel
        self._hw_pi_board_rev = hw_pi_board_rev
        self._hw_cpu_hw = hw_cpu_hw
        self._hw_cpu_rev = hw_cpu_rev
        self._hw_bootloader_ver = hw_bootloader_ver
        self._exec_user = exec_user

    @classmethod
    def from_dict(cls, dikt) -> 'SystemInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemInfo of this SystemInfo.  # noqa: E501
        :rtype: SystemInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def os_kernel(self):
        """Gets the os_kernel of this SystemInfo.

         Current kernel version (retrieved via `uname -srvmo`)  # noqa: E501

        :return: The os_kernel of this SystemInfo.
        :rtype: str
        """
        return self._os_kernel

    @os_kernel.setter
    def os_kernel(self, os_kernel):
        """Sets the os_kernel of this SystemInfo.

         Current kernel version (retrieved via `uname -srvmo`)  # noqa: E501

        :param os_kernel: The os_kernel of this SystemInfo.
        :type os_kernel: str
        """

        self._os_kernel = os_kernel

    @property
    def hw_pi_board_rev(self):
        """Gets the hw_pi_board_rev of this SystemInfo.

        Pi board revision (retrieved via `cat /proc/cpuinfo`)  # noqa: E501

        :return: The hw_pi_board_rev of this SystemInfo.
        :rtype: str
        """
        return self._hw_pi_board_rev

    @hw_pi_board_rev.setter
    def hw_pi_board_rev(self, hw_pi_board_rev):
        """Sets the hw_pi_board_rev of this SystemInfo.

        Pi board revision (retrieved via `cat /proc/cpuinfo`)  # noqa: E501

        :param hw_pi_board_rev: The hw_pi_board_rev of this SystemInfo.
        :type hw_pi_board_rev: str
        """
        if hw_pi_board_rev is None:
            raise ValueError("Invalid value for `hw_pi_board_rev`, must not be `None`")  # noqa: E501

        self._hw_pi_board_rev = hw_pi_board_rev

    @property
    def hw_cpu_hw(self):
        """Gets the hw_cpu_hw of this SystemInfo.

        Part number of SoC (retrieved via `cat /proc/cpuinfo`)  # noqa: E501

        :return: The hw_cpu_hw of this SystemInfo.
        :rtype: str
        """
        return self._hw_cpu_hw

    @hw_cpu_hw.setter
    def hw_cpu_hw(self, hw_cpu_hw):
        """Sets the hw_cpu_hw of this SystemInfo.

        Part number of SoC (retrieved via `cat /proc/cpuinfo`)  # noqa: E501

        :param hw_cpu_hw: The hw_cpu_hw of this SystemInfo.
        :type hw_cpu_hw: str
        """
        if hw_cpu_hw is None:
            raise ValueError("Invalid value for `hw_cpu_hw`, must not be `None`")  # noqa: E501

        self._hw_cpu_hw = hw_cpu_hw

    @property
    def hw_cpu_rev(self):
        """Gets the hw_cpu_rev of this SystemInfo.

        SoC revision (retrieved via `cat /proc/cpuinfo`)  # noqa: E501

        :return: The hw_cpu_rev of this SystemInfo.
        :rtype: str
        """
        return self._hw_cpu_rev

    @hw_cpu_rev.setter
    def hw_cpu_rev(self, hw_cpu_rev):
        """Sets the hw_cpu_rev of this SystemInfo.

        SoC revision (retrieved via `cat /proc/cpuinfo`)  # noqa: E501

        :param hw_cpu_rev: The hw_cpu_rev of this SystemInfo.
        :type hw_cpu_rev: str
        """
        if hw_cpu_rev is None:
            raise ValueError("Invalid value for `hw_cpu_rev`, must not be `None`")  # noqa: E501

        self._hw_cpu_rev = hw_cpu_rev

    @property
    def hw_bootloader_ver(self):
        """Gets the hw_bootloader_ver of this SystemInfo.

        Current bootloader version (retrieved via `vcgencmd bootloader_version`)  # noqa: E501

        :return: The hw_bootloader_ver of this SystemInfo.
        :rtype: str
        """
        return self._hw_bootloader_ver

    @hw_bootloader_ver.setter
    def hw_bootloader_ver(self, hw_bootloader_ver):
        """Sets the hw_bootloader_ver of this SystemInfo.

        Current bootloader version (retrieved via `vcgencmd bootloader_version`)  # noqa: E501

        :param hw_bootloader_ver: The hw_bootloader_ver of this SystemInfo.
        :type hw_bootloader_ver: str
        """
        if hw_bootloader_ver is None:
            raise ValueError("Invalid value for `hw_bootloader_ver`, must not be `None`")  # noqa: E501

        self._hw_bootloader_ver = hw_bootloader_ver

    @property
    def exec_user(self):
        """Gets the exec_user of this SystemInfo.

        User on the system under which the execution environment (i.e., this app) runs  # noqa: E501

        :return: The exec_user of this SystemInfo.
        :rtype: str
        """
        return self._exec_user

    @exec_user.setter
    def exec_user(self, exec_user):
        """Sets the exec_user of this SystemInfo.

        User on the system under which the execution environment (i.e., this app) runs  # noqa: E501

        :param exec_user: The exec_user of this SystemInfo.
        :type exec_user: str
        """
        if exec_user is None:
            raise ValueError("Invalid value for `exec_user`, must not be `None`")  # noqa: E501

        self._exec_user = exec_user
