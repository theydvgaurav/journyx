class APIException(Exception):
    message = None
    error_code = None
    status_code = 400
    payload = None

    def __init__(self):
        Exception.__init__(self)

    def to_dict(self):
        r = dict(self.payload or ())
        r['message'] = self.message
        r['errorCode'] = self.error_code
        return r
