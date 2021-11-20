###
# Workaround for `https://github.com/OpenAPITools/openapi-generator/issues/4586`
###
from app.web.persistence.db import \
    Config as ConfigLogicModel, \
    FanCurveSeriesPoint as FanCurveSeriesPointLogicModel, \
    FanCurve as FanCurveLogicModel
from app.web.logic.stats import \
    SysStatsSystemInfo as SystemInfoLogicModel, \
    SysStatsOSProcess as SystemProcessLogicModel

from app.web.api.models import \
    AppConfig as ConfigAPIModel, \
    AppFanCurveSeriesPoint as FanCurveSeriesPointAPIModel, \
    AppFanCurve as FanCurveAPIModel, \
    AppFanCurveBase as FanCurveBaseAPIModel
from app.web.api.models import \
    SystemInfo as SystemInfoAPIModel, \
    SystemProcess as SystemProcessAPIModel


def logic_to_apimodel(logic_model_obj):
    if type(logic_model_obj) is ConfigLogicModel:
        return ConfigAPIModel(fan_on=logic_model_obj.fan_on,
                              logging_level=str(logic_model_obj.logging_level),
                              dc_update_interval_in_sec=logic_model_obj.dc_update_interval_in_sec,
                              logging_enabled=logic_model_obj.logging_enabled,
                              selected_fan_curve=logic_to_apimodel(logic_model_obj.selected_fan_curve),
                              pwm_gpio_pin=logic_model_obj.pwm_gpio_pin,
                              pwm_invert_signal=logic_model_obj.pwm_invert_signal,
                              pwm_max_dcin_perc=logic_model_obj.pwm_max_dcin_perc,
                              pwm_min_dcin_perc=logic_model_obj.pwm_min_dcin_perc)

    if type(logic_model_obj) is FanCurveLogicModel:
        return FanCurveAPIModel(
                          did=logic_model_obj.did,
                          name=logic_model_obj.name,
                          fan_curve_series=list(map(logic_to_apimodel, logic_model_obj.fan_curve_series)))

    if type(logic_model_obj) is FanCurveSeriesPointLogicModel:
        return FanCurveSeriesPointAPIModel(
                          temp_in_cels=logic_model_obj.temp_in_cels,
                          fan_dcin_perc=logic_model_obj.fan_dcin_perc)

    if type(logic_model_obj) is SystemInfoLogicModel:
        return SystemInfoAPIModel(
                          exec_user=logic_model_obj.exec_user,
                          hw_bootloader_ver=logic_model_obj.hw_bootloader_ver,
                          hw_cpu_hw=logic_model_obj.hw_cpu_hw,
                          hw_cpu_rev=logic_model_obj.hw_cpu_rev,
                          hw_pi_board_rev=logic_model_obj.hw_pi_board_rev,
                          os_kernel=logic_model_obj.os_kernel)

    if type(logic_model_obj) is SystemProcessLogicModel:
        return SystemProcessAPIModel(
                          cpu_util_in_perc=logic_model_obj.cpu_util_in_perc,
                          name=logic_model_obj.name,
                          pid=logic_model_obj.pid,
                          ppid=logic_model_obj.ppid)

    raise NotImplementedError("Unknown logic model")


def api_to_logicmodel(api_model_obj):
    if type(api_model_obj) is ConfigAPIModel:
        return ConfigLogicModel(
                          fan_on=api_model_obj.fan_on,
                          logging_level=api_model_obj.logging_level,
                          dc_update_interval_in_sec=api_model_obj.dc_update_interval_in_sec,
                          logging_enabled=api_model_obj.logging_enabled,
                          selected_fan_curve=api_to_logicmodel(api_model_obj.selected_fan_curve),
                          pwm_gpio_pin=api_model_obj.pwm_gpio_pin,
                          pwm_invert_signal=api_model_obj.pwm_invert_signal,
                          pwm_max_dcin_perc=api_model_obj.pwm_max_dcin_perc,
                          pwm_min_dcin_perc=api_model_obj.pwm_min_dcin_perc)

    if type(api_model_obj) in [FanCurveAPIModel, FanCurveBaseAPIModel]:
        fan_curve_entity = FanCurveLogicModel(
                          did=None,
                          name=api_model_obj.name,
                          fan_curve_series=list(map(api_to_logicmodel, api_model_obj.fan_curve_series)))
        if type(api_model_obj) is FanCurveAPIModel:
            fan_curve_entity.did = api_model_obj.did
        return fan_curve_entity

    if type(api_model_obj) is FanCurveSeriesPointAPIModel:
        return FanCurveSeriesPointLogicModel(
                          temp_in_cels=api_model_obj.temp_in_cels,
                          fan_dcin_perc=api_model_obj.fan_dcin_perc)

    raise NotImplementedError("Unknown api model")
