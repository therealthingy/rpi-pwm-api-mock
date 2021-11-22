import logging

import connexion
from flask_testing import TestCase


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../')
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app
