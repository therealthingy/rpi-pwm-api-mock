import enum
import uuid
from app.web.persistence.db import db


class FanCurve(db.Model):
    __tablename__ = "fan_curve"

    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    fanCurveSeries = db.relationship("FanCurveSeriesPoint", backref="fan_curve",
                                     lazy=False)  # One-To-Many unidirectional FanCurve -> FanCurveSeriesPoint

class FanCurveSeriesPoint(db.Model):
    __tablename__ = "fan_curve_point"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fanDcInPerc = db.Column(db.Integer, nullable=False)  # TODO: min = 0, max = 100
    tempInCels = db.Column(db.Integer, nullable=False)
    fanCurve_id = db.Column(db.String(255), db.ForeignKey('fan_curve.id'))


class LoggingLevel(enum.Enum):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    CRITICAL = 5

class Config(db.Model):
    '''
    Shall be a SINGLETON
    '''
    __tablename__ = "config"

    id = db.Column(db.Integer, primary_key=True, default=0)
    DCUpdateInternalInSec = db.Column(db.Integer, nullable=False)
    fanOn = db.Column(db.Boolean, nullable=False)
    loggingEnabled = db.Column(db.Boolean, nullable=False)
    loggingLevel = db.Column(db.Enum(LoggingLevel), nullable=False)
    selectedFanCurve_id = db.Column(db.String(255),
                                    db.ForeignKey(FanCurve.id))  # One-To-One unidirectional Config -> FanCurve
    selectedFanCurve = db.relationship(FanCurve, uselist=False, lazy=False)

    # def __repr__(self):
    #     return 'ItemModel(id=%d,name=%s, price=%s,)' % (self.id, self.name, self.price)
    #
    # def json(self):
    #     return {'id':self.id,'name': self.name, 'price': self.price}