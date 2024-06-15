import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Adicione outras configurações comuns aqui

class DefaultConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI', 'postgresql://postgres:2112@localhost:5432/propagandas')

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI', 'postgresql://postgres:2112@localhost:5432/propagandas')

class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql://postgres:2112@localhost:5432/propagandas')

config = {
    'development': DefaultConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DefaultConfig
}
