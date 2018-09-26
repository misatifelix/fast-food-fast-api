
import os 

class Config(object): 
	"""
	Base config
	"""
	DEBUG = False 
	CSRF_ENABLED = True 
	SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):
	"""
		Config for development
	"""
	DEBUG = True


class TestingConfig(Config): 
	"""
		Testing config
	"""
	Testing = True
	DEBUG = True

class ProductionConfig(Config): 
	"""
		Production config
	"""
	DEBUG = False 
	Testing = False


app_config = {
	'development': DevelopmentConfig, 
	'production': ProductionConfig, 
	'testing': TestingConfig,
}
