# coding: utf-8

class HTTPError(dict):      # By default, `dict`s are JSON serializable
    def __init__(self, http_status_code, http_status_description, app_error_code, app_error_description, log_uuid=None):  # noqa: E501
        """HTTPError - a model defined in OpenAPI

        :param http_status_code: The http_status_code of this HTTPError.  # noqa: E501
        :type http_status_code: int
        :param http_status_description: The http_status_description of this HTTPError.  # noqa: E501
        :type http_status_description: str
        :param app_error_code: The app_error_code of this HTTPError.  # noqa: E501
        :type app_error_code: int
        :param app_error_description: The app_error_description of this HTTPError.  # noqa: E501
        :type app_error_description: str
        :param log_uuid: The log_uuid of this HTTPError.  # noqa: E501
        :type log_uuid: str
        """
        super().__init__(
            httpStatusCode=http_status_code,
            httpStatusDescription=http_status_description,
            appErrorCode=app_error_code,
            appErrorDescription=app_error_description,
            logUuid=log_uuid
        )

    @property
    def http_status_code(self):
        return super().get("httpStatusCode")
