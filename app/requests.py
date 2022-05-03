import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None

base_url = None
sources_url=None
specific_source_articles_url = None

def configure_request(app):
    global api_key,base_url,sources_url,specific_source_articles_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    sources_url = app.config['SOURCES_URL']
    specific_source_articles_url = app.config['SPECIFIC_SOURCE_ARTICLES_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(api_key)
    sources_results = [] 
    try:
        with urllib.request.urlopen(get_sources_url) as response:
            if response.status == 200:
                data_ = response.read()
                response_ = json.loads(data_)
                sources_ = response_.get('sources')
                sources_results = process_sources(sources_)         

    except urllib.error.URLError as e:
        print("HTTP ERROR: ", e)
    
    return sources_results


def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain sources details
    Returns :
        source_results: A list of source objects
    '''
    sources = [] 

    for source in sources_list:
        id_ = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        source_object = Source(id_,name,description,url,category,language,country)
        sources.append(source)
    
    return sources 

def get_articles_based_on_source(source_id):
    url_ = specific_source_articles_url.format(source_id, api_key)
    articles = []

    try:

        with urllib.request.urlopen(url_) as response:
            if response.status == 200:
                data_ = response.read()
                response_ = json.loads(data_)
                articles_ = response_.get('articles')
                print(articles_)
                articles = process_articles(articles_)

    except urllib.error.URLError as e:
        print("HTTP ERROR: ", e)

    return articles

def process_articles(article_list):
    articles = []

    for article in article_list:
        source = article.get('source')
        author = article.get('author')
        title = article.get('title')
        image_url = article.get('urlToImage')
        description_ = article.get('description')
        url_ = article.get('url')
        published_at = article.get('publishedAt')
        content = article.get('content')

        article_object = Article(source, author, title, image_url, description_, url_, published_at, content)
        articles.append(article_object)

    return articles


def search_article(article_name):
    
    search_article_url = 'https://newsapi.org/v2/search/articles?api_key={}&query={}'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_articles(search_article_list)


    return search_article_results

# def get_categories():
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_sources_url = sources_url.format(api_key)
#     categories_results = [] 
#     try:
#         with urllib.request.urlopen(get_sources_url) as response:
#             if response.status == 200:
#                 data_ = response.read()
#                 response_ = json.loads(data_)
#                 categories_ = response_.get('categories')
#                 categories_results = process_categories(categories_)         

#     except urllib.error.URLError as e:
#         print("HTTP ERROR: ", e)
    
#     return categories_results

# def process_categories(categories_list):

#     categories = [] 

#     for category in categories_list:
#         general=category.get('general')
#         busines= category.get('business')
#         sports=category.get('sports')
#         entertainment =category.get('entertainment')
#         technology =category.get('technology')
        

#         category_object = Category(general,busines,sports,entertainment,technology)
#         categories.append(category)

#     return categories
