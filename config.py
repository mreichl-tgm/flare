class Config:
    DEBUG = False
    TESTING = False
    DATABASE = 'flare.db'


class Dev(Config):
    DEBUG = True
