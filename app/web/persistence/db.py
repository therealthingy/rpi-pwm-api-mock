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
from sqlalchemy import event, DDL
import enum
import uuid

db = SQLAlchemy()


# ------ ------ ------ ------ ------ ------ ------ Entities + Events ------ ------ ------ ------ ------ ------ ------
class FanCurve(db.Model):
    __tablename__ = "fan_curve"

    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    fanCurveSeries = db.relationship("FanCurveSeriesPoint", backref="fan_curve",  lazy=False)  # One-To-Many unidirectional FanCurve -> FanCurveSeriesPoint

@event.listens_for(FanCurve.__table__, 'after_create')
def after_create_fancurve_table(target, connection, **kw):
    connection.execute(
        'INSERT INTO fan_curve (id, name) VALUES ("1C5A8579-AB76-4089-AF15-97FC1F4358AB", "Default");')


class FanCurveSeriesPoint(db.Model):
    __tablename__ = "fan_curve_point"

    id = db.Column(db.Integer, db.Sequence('fan_curve_point_seq', start=4, increment=1), primary_key=True)
    fanDcInPerc = db.Column(db.Integer, nullable=False)  # TODO: min = 0, max = 100
    tempInCels = db.Column(db.Integer, nullable=False)
    fanCurve_id = db.Column(db.String(255), db.ForeignKey('fan_curve.id'))

@event.listens_for(FanCurveSeriesPoint.__table__, 'after_create')
def after_create_fancurvepoint_table(target, connection, **kw):
    connection.execute(
        """INSERT INTO fan_curve_point  (id, fanDcInPerc, tempInCels, fanCurve_id)
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
        return self.name    # Required otherwise `str()` returns e.g., LoggingLevel.WARN instead of just `WARN`

class Config(db.Model):
    __tablename__ = "config"

    id = db.Column(db.Integer, primary_key=True)
    DCUpdateIntervalInSec = db.Column(db.Integer, nullable=False)
    fanOn = db.Column(db.Boolean, nullable=False)
    loggingEnabled = db.Column(db.Boolean, nullable=False)
    loggingLevel = db.Column(db.Enum(LoggingLevel), nullable=False)
    selectedFanCurve_id = db.Column(db.String(255),
                                    db.ForeignKey(FanCurve.id))  # One-To-One unidirectional Config -> FanCurve
    selectedFanCurve = db.relationship(FanCurve, uselist=False, lazy=False)
    pwmGpioPin = db.Column(db.Integer, nullable=False)
    pwmInvertSignal = db.Column(db.Boolean, nullable=False)
    pwmMaxDCInPerc = db.Column(db.Integer, nullable=False)
    pwmMinDCInPerc = db.Column(db.Integer, nullable=False)

@event.listens_for(Config.__table__, 'after_create')
def after_create_config_table(target, connection, **kw):
    connection.execute(
        """INSERT INTO config  (id, DCUpdateIntervalInSec, fanOn, loggingEnabled, loggingLevel, pwmGpioPin,
                                pwmInvertSignal, pwmMaxDCInPerc, pwmMinDCInPerc, selectedFanCurve_id)
           VALUES (0, 3, 0, 1, "WARN", 12, 0, 100, 0, "1C5A8579-AB76-4089-AF15-97FC1F4358AB");""")
