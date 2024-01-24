from flask import Blueprint

from .views.diary import DiaryAPIView

diary_blueprint = Blueprint('diary', __name__)

diary_blueprint.add_url_rule('/diary', view_func=DiaryAPIView.as_view('diary'))
