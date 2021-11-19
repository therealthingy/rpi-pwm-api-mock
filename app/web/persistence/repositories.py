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
    def delete(did) -> None:
        config_repo = ConfigRepo()
        current_config = config_repo.fetch_config()
        if current_config.selectedFanCurve_id == _id:
            raise ValueError("The to be deleted fan curve is currently being used")

        item = db.session.query(FanCurve).filter_by(did=did).first()
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def update(item_data):
        db.session.merge(item_data)
        db.session.commit()


class ConfigRepo:
    @staticmethod
    def fetch_config() -> Config:
        return db.session.query(Config).filter_by(did=0).first()

    @staticmethod
    def update_config(config_data):
        config_data.id = 0                      # Set always to `0` (since Singleton)
        db.session.merge(config_data)
        db.session.commit()