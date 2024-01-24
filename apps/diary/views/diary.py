from base.views.base import BaseView
from middlewares.auth_middleware import require_authentication


class DiaryAPIView(BaseView):
    """"""

    @require_authentication
    def post(self, user, *args, **kwargs):
        return self.get_response("response_data", "response_status")

    def get(self):
        return self.get_response("response_data", "response_status")
