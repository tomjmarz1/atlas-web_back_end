#!/usr/bin/env python3
""" Create a basic Flask App
    with a single '/' route and an index.html template
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from flask import g


class Config:
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
# Use Config class as config for our app
app.config.from_object(Config)

# Instantiate Babel object in module-level variable babel
babel = Babel(app)


# @app.before_request
# def before_request():
#     """ Set/get current language from request
#         and set it to g.locale for Jinja templates to use """
#     g.locale = str(get_locale())


@babel.localeselector
def get_locale():
    """ Return user preferred locale, if not available return best match """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Return index.html template """
    from flask_babel import _  # Marking string for translation
    return render_template('3-index.html',
                           title=_('home_title'),
                           h1=_('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
