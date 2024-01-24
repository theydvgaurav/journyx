class APIException(Exception):

    def __init__(self, message, error_code, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.error_code = error_code

    def to_dict(self):
        r = dict(self.payload or ())
        r['message'] = self.message
        r['errorCode'] = self.error_code
        return r
