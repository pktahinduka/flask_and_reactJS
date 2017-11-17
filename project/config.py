# project/config.py



class BaseConfig:
	"""Base Configurations"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'my_precious'
	SQLALCHEMY_DATABASE_URI = "postgres://postgres:peter926@localhost:5432/users_dev"
	

class DevelopmentConfig:
	"""Development Configurations"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "postgres://postgres:peter926@localhost:5432/users_dev"
    

class ProductionConfig:
	"""Production Configurations"""
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "postgres://postgres:peter926@localhost/users_prod"
    

class TestingConfig:
	"""Testing Configurations"""
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'postgres://postgres:peter926@localhost:5432/users_test'
    