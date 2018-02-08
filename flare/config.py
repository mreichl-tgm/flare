class Config:
    DEBUG = False
    TESTING = False
    MONGO_URI = 'mongodb://canis:ignis@ds113738.mlab.com:13738/flare'
    SECRET_KEY = 'canisignis'


class Dev(Config):
    DEBUG = True


class Test(Config):
    DEBUG = True
    TESTING = True


class Prod(Config):
    pass
