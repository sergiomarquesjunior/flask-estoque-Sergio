import json
import os
import sys

from flask import Flask, render_template

from src.modulos import bootstrap,minify,db
from src.utils import existe_esquema, seeding


def create_app(config_filename: str = 'config.dev.json') -> Flask:
    app = Flask(__name__,
                instance_relative_config=True,
                template_folder='templates',
                static_folder= 'static')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    try:
        app.config.from_file(config_filename, load=json.load)
    except FileNotFoundError:
        app.logger.critical("Não existe o arquivo de configuração informado")
        sys.exit(1)

    bootstrap.init_app(app)
    if app.config.get('MINIFY', False):
        minify.init_app(app)
    db.init_app(app)

    with app.app_context():
        if not existe_esquema(app):
            app.logger.critical("Efatuar a migração/upgrade do banco")
            sys.exit(1)

        if app.config.get('SEEDING', False):
            seeding(db)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.jinja',
                               title="Página principal")

    return app

