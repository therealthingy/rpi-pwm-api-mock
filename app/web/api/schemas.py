from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields as sql_fields
from marshmallow import Schema, fields

from app.web.persistence.db import FanCurve, FanCurveSeriesPoint, Config
from app.web.logic.history import AppLogEntry, AppTempDCHistoryEntry
from app.web.logic.sysinfo import SysStatsSystemInfo, SysStatsOSProcess


# -- Custom schema types --
def _camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class _SQLAlchemyAutoCamelCaseSchema(SQLAlchemyAutoSchema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """
    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = _camelcase(field_obj.data_key or field_name)


class _CaseSchema(Schema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """
    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = _camelcase(field_obj.data_key or field_name)


# -- Schemas --
class FanCurveSeriesPointSchema(_SQLAlchemyAutoCamelCaseSchema):
    class Meta:
        model = FanCurveSeriesPoint
        load_instance = True
        exclude = ("did",)


class FanCurveSchema(_SQLAlchemyAutoCamelCaseSchema):
    class Meta:
        model = FanCurve
        load_instance = True

    fan_curve_series = sql_fields.Nested(FanCurveSeriesPointSchema, many=True)


class ConfigSchema(_SQLAlchemyAutoCamelCaseSchema):
    class Meta:
        model = Config
        load_instance = True
        exclude = ("did",)

    selected_fan_curve = sql_fields.Nested(FanCurveSchema)


class SysStatsSystemInfoSchema(_CaseSchema):
    class Meta:
        model = SysStatsSystemInfo
        load_instance = True

    exec_user = fields.String()
    hw_bootloader_ver = fields.String()
    hw_cpu_hw = fields.String()
    hw_cpu_rev = fields.String()
    hw_pi_board_rev = fields.String()
    os_kernel = fields.String()


class SysStatsOSProcessSchema(_CaseSchema):
    class Meta:
        model = SysStatsOSProcess
        load_instance = True

    cpu_util_in_perc = fields.Float()
    name = fields.String()
    pid = fields.Integer()
    ppid = fields.Integer()


class AppLogEntrySchema(_CaseSchema):
    class Meta:
        model = AppLogEntry
        load_instance = True

    date = fields.DateTime()
    level = fields.String()
    message = fields.String()
    uuid = fields.String()


class AppTempDCHistoryEntrySchema(_CaseSchema):
    class Meta:
        model = AppTempDCHistoryEntry
        load_instance = True

    date = fields.DateTime()
    fan_dc_in_perc = fields.Integer()
    temp_in_cels = fields.Integer()
