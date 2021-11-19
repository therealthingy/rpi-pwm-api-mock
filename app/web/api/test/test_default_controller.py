# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from app.web.api.models.app_config import AppConfig  # noqa: E501
from app.web.api.models.app_fan_curve import AppFanCurve  # noqa: E501
from app.web.api.models.app_fan_curve_base import AppFanCurveBase  # noqa: E501
from app.web.api.models.app_log_entry import AppLogEntry  # noqa: E501
from app.web.api.models.app_temp_dc_history_entry import AppTempDCHistoryEntry  # noqa: E501
from app.web.api.models.system_info import SystemInfo  # noqa: E501
from app.web.api.models.system_process import SystemProcess  # noqa: E501
from app.web.api.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_app_config_get(self):
        """Test case for app_config_get

        Returns current config flags
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/config',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_config_put(self):
        """Test case for app_config_put

        Updates config flags
        """
        app_config = {
  "fanOn" : true,
  "loggingEnabled" : true,
  "loggingLevel" : "WARN",
  "DCUpdateIntervalInSec" : 3,
  "selectedFanCurve" : {
    "did" : "916CD0EB-A755-4663-8410-461431039F74",
    "name" : "Quiet",
    "fanCurveSeries" : [ {
      "tempInCels" : 30,
      "fanDCInPerc" : 40
    }, {
      "tempInCels" : 35,
      "fanDCInPerc" : 50
    } ]
  },
  "pwmGpioPin" : 12,
  "pwmInvertSignal" : true,
  "pwmMinDCInPerc" : 20,
  "pwmMaxDCInPerc" : 95
}
        headers = { 
            'if_match': 'b5395865858689cfcb718a8fbf84e128771f6975',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/config',
            method='PUT',
            headers=headers,
            data=json.dumps(app_config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_fan_curves_did_delete(self):
        """Test case for app_fan_curves_did_delete

        Deletes fan curve whose id correspond to specified \"did\"
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/fanCurves/{did}'.format(did='4731ab6a-433b-11ec-8321-c3a754deb306'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_fan_curves_did_get(self):
        """Test case for app_fan_curves_did_get

        Returns requested fan curve whose id corresponds to specified \"did\"
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/fanCurves/{did}'.format(did='4731ab6a-433b-11ec-8321-c3a754deb306'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_fan_curves_did_put(self):
        """Test case for app_fan_curves_did_put

        Updates requested fan curve whose id corresponds to specified \"did\"
        """
        app_fan_curve_base = {
  "name" : "Quiet",
  "fanCurveSeries" : [ {
    "tempInCels" : 30,
    "fanDCInPerc" : 40
  }, {
    "tempInCels" : 35,
    "fanDCInPerc" : 50
  } ]
}
        headers = { 
            'if_match': 'b5395865858689cfcb718a8fbf84e128771f6975',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/fanCurves/{did}'.format(did='4731ab6a-433b-11ec-8321-c3a754deb306'),
            method='PUT',
            headers=headers,
            data=json.dumps(app_fan_curve_base),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_fan_curves_get(self):
        """Test case for app_fan_curves_get

        Returns list of all available fan curves
        """
        query_string = [('name', 'Quiet-')]
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/fanCurves',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_fan_curves_post(self):
        """Test case for app_fan_curves_post

        Adds new fan curve
        """
        app_fan_curve_base = {
  "name" : "Quiet",
  "fanCurveSeries" : [ {
    "tempInCels" : 30,
    "fanDCInPerc" : 40
  }, {
    "tempInCels" : 35,
    "fanDCInPerc" : 50
  } ]
}
        query_string = [('name', 'Quiet-')]
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/fanCurves',
            method='POST',
            headers=headers,
            data=json.dumps(app_fan_curve_base),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_logs_get(self):
        """Test case for app_logs_get

        Returns list of all available fan curves
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/logs/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_temp_dc_history_get(self):
        """Test case for app_temp_dc_history_get

        Returns temperature- & fan history over last 10 min.
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/app/tempDCHistory',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_info_get(self):
        """Test case for system_info_get

        Returns information about used system (SW & HW)
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/system/info',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_top_ten_processes_get(self):
        """Test case for system_top_ten_processes_get

        Returns list of top 10 processes using the most CPU time
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/system/topTenProcesses',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_top_ten_processes_nr_get(self):
        """Test case for system_top_ten_processes_nr_get

        Returns requested process whose current CPU utilization corresponds to specified nr in ranking
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/v1/system/topTenProcesses/{nr}'.format(nr=2),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
