#!/usr/bin/env python3
"""Simple flask app with index.html template"""
from flask import Flask, render_template, request, g
from flask_babel import Babel




class Config():
    """Class which configures available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Retrieves locale from request"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request():
    """ Set/get current language from request """
    g.locale = str(get_locale())
    refresh()

@app.route('/', strict_slashes=False)
def index():
    """Route for `/`"""
    return render_template('4-index.html')




if __name__ == '__main__':
    app.run()
