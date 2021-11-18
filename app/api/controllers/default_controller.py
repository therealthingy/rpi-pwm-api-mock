import connexion
import six

from app.api.models.app_config import AppConfig  # noqa: E501
from app.api.models.app_fan_curve_base import AppFanCurveBase  # noqa: E501
from app.api.models.app_fan_curve_complete import AppFanCurveComplete  # noqa: E501
from app.api.models.app_fan_curve_update import AppFanCurveUpdate  # noqa: E501
from app.api.models.app_log_entry import AppLogEntry  # noqa: E501
from app.api.models.app_temp_dc_history_entry import AppTempDCHistoryEntry  # noqa: E501
from app.api.models.http_error import HTTPError  # noqa: E501
from app.api.models.system_info import SystemInfo  # noqa: E501
from app.api.models.system_process import SystemProcess  # noqa: E501
from app.api import util


def app_config_get():  # noqa: E501
    """Returns current config flags

    Returns current config flags # noqa: E501


    :rtype: AppConfig
    """
    return 'do some magic!'


def app_config_put(body):  # noqa: E501                       # ?? WHY NEED TO CHANGE TO `body` ??
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

    :rtype: List[AppFanCurveComplete]
    """
    return 'do some magic!'


def app_fan_curves_id_delete(id_):  # noqa: E501                       # ?? WHY IS HERE A `_` necessary ??
    """Deletes fan curve whose id correspond to specified \&quot;id\&quot;

    Deletes fan curve whose id correspond to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str

    :rtype: None
    """
    return f'do some magic! {id_}'


def app_fan_curves_id_get(id_):  # noqa: E501                       # ?? WHY IS HERE A `_` necessary ??
    """Returns requested fan curve whose id corresponds to specified \&quot;id\&quot;

    Returns requested fan curve whose id corresponds to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str

    :rtype: AppFanCurveComplete
    """
    return f'do some magic! {id_}'


def app_fan_curves_id_put(id_, body):  # noqa: E501                       # ?? WHY IS HERE A `_` necessary ??
    """Updates requested fan curve whose id corresponds to specified \&quot;id\&quot;

    Updates requested fan curve whose id corresponds to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str
    :param app_fan_curve_update: 
    :type app_fan_curve_update: dict | bytes

    :rtype: AppFanCurveComplete
    """
    if connexion.request.is_json:
        app_fan_curve_update = AppFanCurveUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return f'do some magic! {id} {body}'


def app_fan_curves_post(body, name=None):  # noqa: E501                       # ?? WHY NEED TO CHANGE TO `body` ??
    """Adds new fan curve

    Adds new fan curve # noqa: E501

    :param app_fan_curve_base: 
    :type app_fan_curve_base: dict | bytes
    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: AppFanCurveComplete
    """
    if connexion.request.is_json:
        app_fan_curve_base = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
    return f'do some magic! {body}'


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
