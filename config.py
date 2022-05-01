
import os


class Config:
    API_KEY='1b0f2bd179f44636bef9b3fe9da611dd'
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