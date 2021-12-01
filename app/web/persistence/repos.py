"""
Used for performing CRUD operations on db through ORM
"""
from app.web.persistence.db import db, FanCurve, Config
from typing import List


class FanCurveRepo:
    @staticmethod
    def create(fan_curve):
        db.session.add(fan_curve)
        db.session.commit()

    @staticmethod
    def find_by_id(did) -> FanCurve:
        return db.session.query(FanCurve).filter_by(did=did).first()

    @staticmethod
    def find_all(name=None) -> List[FanCurve]:
        return db.session.query(FanCurve).all() if name is None else \
            db.session.query(FanCurve).filter(FanCurve.name.startswith(name)).all()

    @staticmethod
    def delete(did) -> bool:
        config_repo = ConfigRepo()
        current_config = config_repo.fetch_config()
        if current_config.selected_fancurve_did == did:
            raise ValueError("The to be deleted fan curve is currently being used")

        fan_curve = db.session.query(FanCurve).filter_by(did=did).first()
        if not (fan_curve is None):
            db.session.delete(fan_curve)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def update(fan_curve):
        db.session.merge(fan_curve)
        db.session.commit()


class ConfigRepo:
    @staticmethod
    def fetch_config() -> Config:
        return db.session.query(Config).filter_by(did=0).first()

    @staticmethod
    def update_config(config):
        if config.pwm_min_dc_in_perc >= config.pwm_max_dc_in_perc:
            raise ValueError("max value for pwm has to be greater than the min value")

        found_selected_fan_curve = FanCurveRepo.find_by_id(config.selected_fan_curve.did)
        if found_selected_fan_curve is None:
            raise ValueError("Provided `selectedFanCurve` doesn't exist")

        config.selected_fan_curve = found_selected_fan_curve
        config.did = 0                  # Set always to `0` (since Singleton)

        db.session.merge(config)
        db.session.commit()