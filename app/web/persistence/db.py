"""
Creates db object containing db config + model (entities)

  Testing:
    0. eval "$(pdm --pep582)" && python
    1. from flask import Flask
       app = Flask(__name__)
    2. import entities
    3. db.create_all()

    import importlib
    importlib.reload(entities)
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
import enum
import uuid

db = SQLAlchemy()


# ------ ------ ------ ------ ------ ------ ------ Entities + Events ------ ------ ------ ------ ------ ------ ------
class FanCurve(db.Model):
    __tablename__ = "fan_curve"

    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    fan_curve_series = db.relationship("FanCurveSeriesPoint", backref="fan_curve",
                                       lazy=False, cascade="all, delete-orphan")  # One-To-Many unidirectional `FanCurve` -> `FanCurveSeriesPoint`

    # def __iter__(self):                 # Required when deserializing objects of type `Config` (otherwise TypeError b/c FanCurve not iterable)
    #     for attr in dir(self):
    #         if not attr.startswith("__"):
    #             yield attr

@event.listens_for(FanCurve.__table__, 'after_create')
def after_create_fancurve_table(target, connection, **kw):
    connection.execute(
        'INSERT INTO fan_curve (id, name) VALUES ("1C5A8579-AB76-4089-AF15-97FC1F4358AB", "Default");')


class FanCurveSeriesPoint(db.Model):
    __tablename__ = "fan_curve_point"

    id = db.Column(db.Integer, db.Sequence('fan_curve_point_seq', start=4, increment=1), primary_key=True)
    fan_dcin_perc = db.Column(db.Integer, nullable=False)  # TODO: min = 0, max = 100
    temp_in_cels = db.Column(db.Integer, nullable=False)
    fan_curve_id = db.Column(db.String(255), db.ForeignKey('fan_curve.id'))

@event.listens_for(FanCurveSeriesPoint.__table__, 'after_create')
def after_create_fancurvepoint_table(target, connection, **kw):
    connection.execute(
        """INSERT INTO fan_curve_point  (id, fan_dcin_perc, temp_in_cels, fan_curve_id)
            VALUES
                (0,  0, 45, "1C5A8579-AB76-4089-AF15-97FC1F4358AB"),
                (1,  30, 46, "1C5A8579-AB76-4089-AF15-97FC1F4358AB"),
                (2, 50, 60, "1C5A8579-AB76-4089-AF15-97FC1F4358AB"),
                (3, 60, 100, "1C5A8579-AB76-4089-AF15-97FC1F4358AB");""")


class LoggingLevel(enum.Enum):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    CRITICAL = 5

    def __str__(self):
        return self.name            # Required for deserialization -> otherwise `str()` returns e.g., `LoggingLevel.WARN` instead of just `WARN`


class Config(db.Model):
    __tablename__ = "config"

    id = db.Column(db.Integer, primary_key=True)
    dc_update_interval_in_sec = db.Column(db.Integer, nullable=False)
    fan_on = db.Column(db.Boolean, nullable=False)
    logging_enabled = db.Column(db.Boolean, nullable=False)
    logging_level = db.Column(db.Enum(LoggingLevel), nullable=False)
    selected_fancurve_id = db.Column(db.String(255),
                                    db.ForeignKey(FanCurve.id))  # One-To-One unidirectional Config -> FanCurve
    selected_fan_curve = db.relationship(FanCurve, uselist=False, lazy=False)
    pwm_gpio_pin = db.Column(db.Integer, nullable=False)
    pwm_invert_signal = db.Column(db.Boolean, nullable=False)
    pwm_max_dcin_perc = db.Column(db.Integer, nullable=False)
    pwm_min_dcin_perc = db.Column(db.Integer, nullable=False)

    # def __iter__(self):             # Required when deserializing object (otherwise TypeError b/c FanCurve not iterable)
    #     for attr in dir(self):
    #         if not attr.startswith("__"):
    #             yield attr

@event.listens_for(Config.__table__, 'after_create')
def after_create_config_table(target, connection, **kw):
    connection.execute(
        """INSERT INTO config  (id, dc_update_interval_in_sec, fan_on, logging_enabled, logging_level, pwm_gpio_pin,
                                pwm_invert_signal, pwm_max_dcin_perc, pwm_min_dcin_perc, selected_fancurve_id)
           VALUES (0, 3, 0, 1, "WARN", 12, 0, 100, 0, "1C5A8579-AB76-4089-AF15-97FC1F4358AB");""")
