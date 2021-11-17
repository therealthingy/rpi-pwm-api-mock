import connexion
import six

from ..models.app_config import AppConfig  # noqa: E501
from ..models.app_fan_curve import AppFanCurve  # noqa: E501
from ..models.app_fan_curve_base import AppFanCurveBase  # noqa: E501
from ..models.app_log_entry import AppLogEntry  # noqa: E501
from ..models.app_temp_dc_history_entry import AppTempDCHistoryEntry  # noqa: E501
from ..models.http_error import HTTPError  # noqa: E501
from ..models.system_info import SystemInfo  # noqa: E501
from ..models.system_process import SystemProcess  # noqa: E501
from .. import util


def app_config_get():  # noqa: E501
    """Returns current config flags

    Returns current config flags # noqa: E501


    :rtype: AppConfig
    """
    return 'do some magic!'


def app_config_put(app_config):  # noqa: E501
    """Updates config flags

    Updates config flags # noqa: E501

    :param app_config: Config flags consisting of app and pwm config
    :type app_config: dict | bytes

    :rtype: AppConfig
    """
    if connexion.request.is_json:
        app_config = AppConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_fan_curves_get(name=None):  # noqa: E501
    """Returns list of all available fan curves

    Returns list of all available fan curves # noqa: E501

    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: List[AppFanCurve]
    """
    return 'do some magic!'


def app_fan_curves_id_delete(id):  # noqa: E501
    """Deletes fan curve whose id correspond to specified \&quot;id\&quot;

    Deletes fan curve whose id correspond to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def app_fan_curves_id_get(id):  # noqa: E501
    """Returns requested fan curve whose id corresponds to specified \&quot;id\&quot;

    Returns requested fan curve whose id corresponds to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str

    :rtype: AppFanCurve
    """
    return 'do some magic!'


def app_fan_curves_id_put(id, app_fan_curve_base):  # noqa: E501
    """Updates requested fan curve whose id corresponds to specified \&quot;id\&quot;

    Updates requested fan curve whose id corresponds to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str
    :param app_fan_curve_base: 
    :type app_fan_curve_base: dict | bytes

    :rtype: AppFanCurve
    """
    if connexion.request.is_json:
        app_fan_curve_base = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_fan_curves_post(app_fan_curve_base, name=None):  # noqa: E501
    """Adds new fan curve

    Adds new fan curve # noqa: E501

    :param app_fan_curve_base: 
    :type app_fan_curve_base: dict | bytes
    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: AppFanCurve
    """
    if connexion.request.is_json:
        app_fan_curve_base = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_logs_get():  # noqa: E501
    """Returns list of all available fan curves

    Returns list of all available fan curves # noqa: E501


    :rtype: List[AppLogEntry]
    """
    return 'do some magic!'


def app_temp_dc_history_get():  # noqa: E501
    """Returns temperature- &amp; fan history over last 10 min.

    Returns temperature- &amp; fan history over last 10 min. # noqa: E501


    :rtype: List[AppTempDCHistoryEntry]
    """
    return 'do some magic!'


def system_info_get():  # noqa: E501
    """Returns information about used system (SW &amp; HW)

    Returns information about used system (SW &amp; HW) # noqa: E501


    :rtype: SystemInfo
    """
    return 'do some magic!'


def system_top_ten_processes_get():  # noqa: E501
    """Returns list of top 10 processes using the most CPU time

    Returns list of top 10 processes using the most CPU time # noqa: E501


    :rtype: List[SystemProcess]
    """
    return 'do some magic!'


def system_top_ten_processes_nr_get(nr):  # noqa: E501
    """Returns requested process whose current CPU utilization corresponds to specified nr in ranking

    Returns requested process whose current CPU utilization corresponds to specified &#x60;nr&#x60; in ranking # noqa: E501

    :param nr: Corresponds to process w/ &#x60;nr&#x60; highest CPU utilization at current moment
    :type nr: int

    :rtype: SystemProcess
    """
    return 'do some magic!'
