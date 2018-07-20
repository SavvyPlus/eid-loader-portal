class Config(object):
    DEBUG = False
    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    # for wtf form
    WTF_CSRF_SECRET_KEY = 'a random string'
    PREFIX_INV_IN_FOLDER = ""


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    PREFIX_INV_IN_FOLDER = "tmp/"
