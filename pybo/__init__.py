from flask import Flask
import config


def create_app():
    # flask 애플리케이션을 생성하는 코드
    app = Flask(__name__)
    # app.config.from_object(config) 
    app.config.from_envvar('APP_CONFIG_FILE')  # 환경 변수에서 APP_CONFIG_FILE을 읽어온다. 

    # blueprint 등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    
    return app


