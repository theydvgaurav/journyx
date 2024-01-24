from pathlib import Path

from flask import Flask
from flask_cors import CORS

from apps.diary.blueprint import diary_blueprint
from apps.users.blueprint import users_blueprint
from base.exception_handler.exception_handler import error_handler_blueprint
from common.logging.logger import JournyxLogger

config_path = Path(__file__).with_name("logging_conf.json")
print(config_path)
journyx_logger = JournyxLogger.make_logger(config_path)

app = Flask(__name__)
CORS(app)

app.register_blueprint(error_handler_blueprint)
app.register_blueprint(diary_blueprint, url_prefix='/v1')
app.register_blueprint(users_blueprint, url_prefix='/v1')

if __name__ == '__main__':
    app.run(port=4070, debug=True)
