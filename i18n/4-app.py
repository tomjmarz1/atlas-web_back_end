#!/usr/bin/env python3
""" Create a basic Flask App
    with a single '/' route and an index.html template
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, refresh


class Config:
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
# Use Config class as config for our app
app.config.from_object(Config)

# Instantiate Babel object in module-level variable babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Return user preferred locale, if not available return best match """
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale
    # if not in url, check user browser settings
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """ Set/get current language from request """
    g.locale = str(get_locale())
    refresh()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Return index.html template """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
