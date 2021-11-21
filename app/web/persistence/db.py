"""
Creates db object containing db config + model (entities)
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from enum import Enum
import uuid

from app.common.decorators import auto_str, auto_repr, auto_iter


# -- Globals --
db = SQLAlchemy()


# ------ ------ ------ ------ ------ ------ ------ Entities + Events ------ ------ ------ ------ ------ ------ ------
@auto_iter(exclude_vars=None)
@auto_str(exclude_vars=None)
@auto_repr(exclude_vars=None)          # Required for ETag
class FanCurve(db.Model):
    __tablename__ = "fan_curve"

    did = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    fan_curve_series = db.relationship("FanCurveSeriesPoint", backref="fan_curve",
                                       lazy=False, cascade="all, delete-orphan")  # One-To-Many unidirectional `FanCurve` -> `FanCurveSeriesPoint`


@event.listens_for(FanCurve.__table__, 'after_create')
def after_create_fancurve_table(target, connection, **kw):
    connection.execute(
        'INSERT INTO fan_curve (did, name) VALUES ("1c5a8579-ab76-4089-af15-97fc1f4358ab", "Default");')


# @auto_iter(exclude_vars=None)
@auto_str(exclude_vars=None)
@auto_repr(exclude_vars=None)           # Required for ETag
class FanCurveSeriesPoint(db.Model):
    __tablename__ = "fan_curve_point"

    did = db.Column(db.Integer, db.Sequence('fan_curve_point_seq', start=4, increment=1), primary_key=True)
    fan_dc_in_perc = db.Column(db.Integer, nullable=False)  # TODO: min = 0, max = 100
    temp_in_cels = db.Column(db.Integer, nullable=False)
    fan_curve_did = db.Column(db.String(255), db.ForeignKey('fan_curve.did'))


@event.listens_for(FanCurveSeriesPoint.__table__, 'after_create')
def after_create_fancurvepoint_table(target, connection, **kw):
    connection.execute(
        """INSERT INTO fan_curve_point (did, fan_dc_in_perc, temp_in_cels, fan_curve_did)
            VALUES
                (0,  0, 45, "1c5a8579-ab76-4089-af15-97fc1f4358ab"),
                (1,  30, 46, "1c5a8579-ab76-4089-af15-97fc1f4358ab"),
                (2, 50, 60, "1c5a8579-ab76-4089-af15-97fc1f4358ab"),
                (3, 60, 100, "1c5a8579-ab76-4089-af15-97fc1f4358ab");""")


class LoggingLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __str__(self): return self.name


# @auto_iter(exclude_vars=None)
@auto_str(exclude_vars=None)
@auto_repr(exclude_vars=None)           # Required for ETag
class Config(db.Model):
    __tablename__ = "config"
    __table_args__ = (
        db.CheckConstraint('pwm_min_dc_in_perc < pwm_max_dc_in_perc'),
    )

    did = db.Column(db.Integer, primary_key=True)
    dc_update_interval_in_sec = db.Column(db.Integer, nullable=False)
    fan_on = db.Column(db.Boolean, nullable=False)
    logging_enabled = db.Column(db.Boolean, nullable=False)
    logging_level = db.Column(db.Enum(LoggingLevel), nullable=False)
    selected_fancurve_did = db.Column(db.String(255),
                                    db.ForeignKey(FanCurve.did))  # One-To-One unidirectional Config -> FanCurve
    selected_fan_curve = db.relationship(FanCurve, uselist=False, lazy=False)
    pwm_gpio_pin = db.Column(db.Integer, nullable=False)
    pwm_invert_signal = db.Column(db.Boolean, nullable=False)
    pwm_max_dc_in_perc = db.Column(db.Integer, nullable=False)
    pwm_min_dc_in_perc = db.Column(db.Integer, nullable=False)


@event.listens_for(Config.__table__, 'after_create')
def after_create_config_table(target, connection, **kw):
    connection.execute(
        """INSERT INTO config (did, dc_update_interval_in_sec, fan_on, logging_enabled, logging_level, pwm_gpio_pin,
                               pwm_invert_signal, pwm_max_dc_in_perc, pwm_min_dc_in_perc, selected_fancurve_did)
           VALUES (0, 3, 0, 1, "WARN", 12, 0, 100, 0, "1c5a8579-ab76-4089-af15-97fc1f4358ab");""")
