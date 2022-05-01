import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None

base_url = None
sources_url=None

def configure_request(app):
    global api_key,base_url,sources_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    sources_url = app.config['SOURCES_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
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


def process_sources(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
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
def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results