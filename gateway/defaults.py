#!/usr/bin/env python3

"""Module that contains global variables with the project runtime configuration."""
import datetime
import os
from flask.json import JSONEncoder


def json_serial(obj):
    """Sanitize datetime serialization."""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError('Type {t} not serializable'.format(t=type(obj)))


class JSONEncoderWithExtraTypes(JSONEncoder):
    """JSON Encoder that supports additional types:

        - date/time objects
        - arbitrary non-mapping iterables
    """

    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                return json_serial(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


class F8AConfiguration():
    # keep disabled authentication by default
    DISABLE_AUTHENTICATION = os.getenv('DISABLE_AUTHENTICATION', '1') in ('1', 'True', 'true')

    BAYESIAN_DATA_IMPORTER_SERVICE_PORT = os.getenv("BAYESIAN_DATA_IMPORTER_SERVICE_PORT", 9192)

    BAYESIAN_DATA_IMPORTER_SERVICE_HOST = os.getenv("BAYESIAN_DATA_IMPORTER_SERVICE_HOST", "data-model-importer")

    DATA_IMPORTER_ENDPOINT = "http://%s:%s" % (BAYESIAN_DATA_IMPORTER_SERVICE_HOST, BAYESIAN_DATA_IMPORTER_SERVICE_PORT)

    BAYESIAN_JWT_AUDIENCE = os.getenv("BAYESIAN_JWT_AUDIENCE", "fabric8-online-platform")


configuration = F8AConfiguration()
