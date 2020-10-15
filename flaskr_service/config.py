"""
  this file is config for flask with prod, dev, test Env.
"""


class Config(object):
    """
      default config
    """
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 5000
    REDIS_DB_URL = {
        'host': '127.0.0.1',
        'port': 6379,
        'password': 'xiangyu1991',
        'db': 0
    }


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
