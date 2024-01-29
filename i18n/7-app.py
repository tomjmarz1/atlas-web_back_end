#!/usr/bin/env python3
"""Simple flask app with index.html template"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from typing import Dict, List, Optional


app: Flask = Flask(__name__)

users: Dict[int, dict] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Class which configures available languages"""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> None:
    """Route for `/`"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """Retrieves locale from request"""
    # Try to get locale from URL parameters
    locale: str = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Try to get locale from user settings
    user: Optional[dict] = get_user()
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')

    # Try to get locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves timezone"""
    timezone: str = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    user: Optional(dict) = get_user()
    if user and user.get('timezone'):
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
        return user.get('timezone')

    return 'UTC'


def get_user():
    """Returns a user dictionary"""
    user_id: Optional(dict) = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Uses get_user to find a user and sets it as a global
    on flask.g.user
    """
    g.user: Optional(dict) = get_user()


if __name__ == '__main__':
    app.run()
