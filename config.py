from distutils.debug import DEBUG
import os


class Config:
    API_KEY='cd75cc1a141e4844980dd4f4bc2fc377'
    BASE_URL='https://newsapi.org/v2/everything?apiKey={}'
    SOURCES_URL='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    SPECIFIC_SOURCE_ARTICLES_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):
    DEBUG=False

class DevConfig(Config):
    DEBUG=True

config_options={
    'produnction':ProdConfig,
    'development':DevConfig
}