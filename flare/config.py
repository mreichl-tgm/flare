class Config:
    DEBUG = False
    TESTING = False


class Dev(Config):
    DEBUG = True


class Test(Config):
    DEBUG = True
    TESTING = True


class Prod(Config):
    pass
