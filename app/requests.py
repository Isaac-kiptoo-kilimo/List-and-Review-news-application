import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    sources_url = app.config['SOURCES_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key) 
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data) 

        sources_result = None 

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_result = process_results(sources_results_list)  

    return sources_result


def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = [] 

    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster: # check if the movie_item has a poster
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count) # create the movie object. 
            movie_results.append(movie_object)
    
    return movie_results 

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