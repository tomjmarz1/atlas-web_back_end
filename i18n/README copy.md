# PROJECT: i18n

AUTHOR: Matthew Allen

## TASKS:

### 0. Basic Flask app - `0-app.py`, `templates/0-index.html`

Sets up a basic Flask app in `0-ap.py` with a single `/` route and an `index.html` template that simply outputs "Welcome to Holberton" as page title (`<title>`) and "Hello world" as header (`<h1>`).

### 1. Basic Babel setup - `1-app.py`, `templates/1-index.html`

Instantiates a `Babel` object in the ap, storing it in a module-level variable named `babel`.
In order to configure available languages in the app, creates a `Config` class which has a `LANGUAGES` class attribute equal to `["en", "fr"]`.
Uses `Config` to set Babel's default locale (`"en"`) and timezone (`"UTC"`).

### 2. Get locale from request - `2-app.py`, `templates/2-index.html`

Creates a `get_locale` function with the `babel.localeselector` decorator.  Uses `request.acceps_languages` to determine the best match with our supported languages.

### 3. Parameterize templates - `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`

Uses the `_` or `gettext` function to parametrize the templates.  Uses the message IDs `home_title` and `home_header`.
Creates a `babel.cfg` file containing

    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_

Then initializes translations with

    $ pybabel extract -F babel.cfg -o messages.pot .

and two dictionaries with

    $ pybabel init -i messages.pot -d translations -l en
    $ pybabel init -i messages.pot -d translations -l fr

Finally, edits files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language, using the following translations:

|msgid | English | French |
| ---- | ------- | ------ |
| home_title | "Welcome to Holberton" | "Bienvenue chez Holberton" |
| home_header | "Hello world!" | "Bonjour monde!" |

Dictionaries are compiled with

    $ pybabel compile -d translations

### 4. Force locale with URL parameter - `4-app.py`, `templates/4-index.html`

Implements a way to force a particular locale by passing the `locale=fr` parameter to the app's URLs.
In the `get_locale` function, detects if the incoming request contains the `locale` argument and if its value is a supported locale, returns it.  If not or if the parameter is not present, resorts to the previous default behavior.

Translations are tested by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

### 5. Mock logging in - `5-app.py`, `templates/5-index.html`

Emulates a user-login system by mocking a database user table:

    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }

Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Defines a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Defines a `before_request` function and uses the `app.before_request` decorator to make it be executed before all other functions.  `before_request` uses `get_user` to find a user if any, and sets it as a global on `flask.g.user`.

In the HTML template, if a user is logged in, in a paragraph tab, displays a welcome message otherwise displays a default message as shown in the table below:

| msgid | English | French |
| ----- | ------- | ------ |
| logged_in_as | "You are logged in as %(username)s." | "Vous êtes connecté en tant que %(username)s." |
| not_logged_in | "You are not logged in." | "Vous n'êtes pas connecté." |

### 6. Use user locale - `6-app.py`, `templates/6-index.html`

Changes `get_locale` function to use a user's preferred locale if it is supported.

The order of priority should be

1. Locale from URL parameters
2. Locale from user settings
3. Locale from request header
4. Default locale

### 7. Infer appropriate time zone - `7-app.py`, `templates/7-index.html`

Defines a `get_timezone` function and uses the `babel.timezoneselector` decorator.

The logic is the same as `get_locale`:

1. Find `timezone` parameter in URL parameters
2. Find time zone from user settings
3. Default to UTC

Before returning a URL-provided or user time sonze, validates that it is a valid time zone.  To do so, uses `pytz.timezone` and catches the `pytz.exceptions.UnknownTimeZoneError` exception.