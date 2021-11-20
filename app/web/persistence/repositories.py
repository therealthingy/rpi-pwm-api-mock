from app.web.persistence.db import db, FanCurve, Config
from typing import List


class FanCurveRepo:
    @staticmethod
    def create(fan_curve):
        db.session.add(fan_curve)
        db.session.commit()

    @staticmethod
    def fetch_by_id(did) -> FanCurve:
        return db.session.query(FanCurve).filter_by(did=did).first()

    @staticmethod
    def fetch_all() -> List[FanCurve]:
        return db.session.query(FanCurve).all()

    @staticmethod
    def delete(did) -> bool:
        config_repo = ConfigRepo()
        current_config = config_repo.fetch_config()
        if current_config.selected_fancurve_did == did:
            raise ValueError("The to be deleted fan curve is currently being used")

        fan_curve = db.session.query(FanCurve).filter_by(did=did).first()
        if fan_curve is not None:
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
        config.did = 0                      # Set always to `0` (since Singleton)
        db.session.merge(config)
        db.session.commit()