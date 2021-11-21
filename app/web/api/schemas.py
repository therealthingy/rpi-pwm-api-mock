"""
Schema used by marshmallow to convert b/w API json request & entities / models used by backend
    Note: To get the endpoint names, evaluate `connex_app.app.url_map`
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields as sql_fields
from marshmallow import Schema, fields
from app.web.backend import ma

from app.web.persistence.db import FanCurve, FanCurveSeriesPoint, Config
from app.web.logic.history import AppLogEntry, AppTempDCHistoryEntry
from app.web.logic.sysinfo import SysStatsSystemInfo, SysStatsOSProcess


# -- Custom schema types --
def _attr_to_camelcase(attr):
    parts = iter(attr.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


def with_camel_case(*, excluded_fields=None):
    if excluded_fields is None:
        excluded_fields = []
    def wrapper(cls):
        def on_bind_field(self, field_name, field_obj):
            value = field_obj.data_key or field_name
            field_obj.data_key = _attr_to_camelcase(value) if value not in excluded_fields else value
        cls.on_bind_field = on_bind_field
        return cls
    return wrapper


# -- Schemas --
@with_camel_case(excluded_fields=None)
class FanCurveSeriesPointSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FanCurveSeriesPoint
        load_instance = True
        exclude = ("did",)


@with_camel_case(excluded_fields=("_links",))
class FanCurveSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FanCurve
        load_instance = True

    fan_curve_series = sql_fields.Nested(FanCurveSeriesPointSchema, many=True)

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("/api/v1.app_web_api_controllers_api_controller_app_fan_curves_did_get", values=dict(did="<did>")),
            "collection": ma.URLFor("/api/v1.app_web_api_controllers_api_controller_app_fan_curves_get")
        }
    )


@with_camel_case(excluded_fields=None)
class ConfigSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Config
        load_instance = True
        exclude = ("did",)

    selected_fan_curve = sql_fields.Nested(FanCurveSchema)


@with_camel_case(excluded_fields=None)
class SysStatsSystemInfoSchema(Schema):
    class Meta:
        model = SysStatsSystemInfo
        load_instance = True

    exec_user = fields.String()
    hw_bootloader_ver = fields.String()
    hw_cpu_hw = fields.String()
    hw_cpu_rev = fields.String()
    hw_pi_board_rev = fields.String()
    os_kernel = fields.String()


@with_camel_case(excluded_fields=("_links",))
class SysStatsOSProcessSchema(Schema):
    class Meta:
        model = SysStatsOSProcess
        load_instance = True

    cpu_util_in_perc = fields.Float()
    name = fields.String()
    pid = fields.Integer()
    ppid = fields.Integer()

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {   # Singleton doesn't make sense due to dynamic nature of results
            "collection": ma.URLFor("/api/v1.app_web_api_controllers_api_controller_system_top_ten_processes_get")
        }
    )


@with_camel_case(excluded_fields=None)
class AppLogEntrySchema(Schema):
    class Meta:
        model = AppLogEntry
        load_instance = True

    date = fields.DateTime()
    level = fields.String()
    message = fields.String()
    uuid = fields.String()


@with_camel_case(excluded_fields=None)
class AppTempDCHistoryEntrySchema(Schema):
    class Meta:
        model = AppTempDCHistoryEntry
        load_instance = True

    date = fields.DateTime()
    fan_dc_in_perc = fields.Integer()
    temp_in_cels = fields.Integer()
