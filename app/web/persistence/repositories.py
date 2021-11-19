from app.web.persistence.db import db, FanCurve, Config
from typing import List


class FanCurveRepo:
    def create(self, fanCurve):
        db.session.add(fanCurve)
        db.session.commit()

    def fetchById(self, _id) -> FanCurve:
        return db.session.query(FanCurve).filter_by(id=_id).first()

    def fetchAll(self) -> List[FanCurve]:
        return db.session.query(FanCurve).all()

    def delete(self, _id) -> None:
        config_repo = ConfigRepo()
        current_config = config_repo.fetchConfig()
        if current_config.selectedFanCurve_id == _id:
            raise ValueError("The to be deleted fan curve is currently being used")

        item = db.session.query(FanCurve).filter_by(id=_id).first()
        db.session.delete(item)
        db.session.commit()

    def update(self, item_data):
        db.session.merge(item_data)
        db.session.commit()


class ConfigRepo:
    def fetchConfig(self) -> Config:
        return db.session.query(FanCurve).filter_by(id=0).first()

    def updateConfig(self, config_data):
        config_data.id = 0                      # Set always to `0` (since Singleton)
        db.session.merge(config_data)
        db.session.commit()