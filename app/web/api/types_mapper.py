###
# Workaround due to `https://github.com/OpenAPITools/openapi-generator/issues/4586`
###
from app.web.persistence.db import \
    Config as ConfigEntity, \
    FanCurveSeriesPoint as FanCurveSeriesPointEntity, \
    FanCurve as FanCurveEntity

from app.web.api.models import \
    AppConfig as ConfigModel, \
    AppFanCurveSeriesPoint as FanCurveSeriesPointModel, \
    AppFanCurve as FanCurveModel


def entity_to_model(db_entity):
    if type(db_entity) is ConfigEntity:
        return ConfigModel(fan_on=db_entity.fan_on,
                           logging_level=str(db_entity.logging_level),
                           dc_update_interval_in_sec=db_entity.dc_update_interval_in_sec,
                           logging_enabled=db_entity.logging_enabled,
                           selected_fan_curve=entity_to_model(db_entity.selected_fan_curve),
                           pwm_gpio_pin=db_entity.pwm_gpio_pin,
                           pwm_invert_signal=db_entity.pwm_invert_signal,
                           pwm_max_dcin_perc=db_entity.pwm_max_dcin_perc,
                           pwm_min_dcin_perc=db_entity.pwm_min_dcin_perc)

    if type(db_entity) is FanCurveEntity:
        return FanCurveModel(
                          id=db_entity.id,
                          name=db_entity.name,
                          fan_curve_series=list(map(entity_to_model, db_entity.fan_curve_series)))

    if type(db_entity) is FanCurveSeriesPointEntity:
        return FanCurveSeriesPointModel(
                          temp_in_cels=db_entity.temp_in_cels,
                          fan_dcin_perc=db_entity.fan_dcin_perc)

    raise NotImplementedError("Unknown type")


def model_to_entity(model_instance):
    if type(model_instance) is ConfigModel:
        return ConfigEntity(
                          fan_on=model_instance.fan_on,
                          logging_level=model_instance.logging_level,
                          dc_update_interval_in_sec=model_instance.dc_update_interval_in_sec,
                          logging_enabled=model_instance.logging_enabled,
                          selected_fan_curve=model_to_entity(model_instance.selected_fan_curve),
                          pwm_gpio_pin=model_instance.pwm_gpio_pin,
                          pwm_invert_signal=model_instance.pwm_invert_signal,
                          pwm_max_dcin_perc=model_instance.pwm_max_dcin_perc,
                          pwm_min_dcin_perc=model_instance.pwm_min_dcin_perc)

    if type(model_instance) is FanCurveModel:
        return FanCurveEntity(
                          id=model_instance.id,
                          name=model_instance.name,
                          fan_curve_series=list(map(model_to_entity, model_instance.fan_curve_series)))

    if type(model_instance) is FanCurveSeriesPointModel:
        return FanCurveSeriesPointEntity(
                          temp_in_cels=model_instance.temp_in_cels,
                          fan_dcin_perc=model_instance.fan_dcin_perc)

    raise NotImplementedError("Unknown type")
