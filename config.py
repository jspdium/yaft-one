
class Config(object):
    DEBUG = False 
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    
class StagingConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    pass
    