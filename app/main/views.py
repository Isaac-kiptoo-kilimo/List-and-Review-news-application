from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles_based_on_source,search_article


@main.route('/')
def index():
  sources = get_sources()
  search_article = request.args.get('article_query')
  if search_article:    
      return redirect(url_for('.search', article_name = search_article)) 
  return render_template('pages/index.html', sources=sources)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(' ')
    article_name_format = "+".join(article_name_list)
    searched_article =search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html', title=title, articles=searched_article)


@main.route('/sources/view/<string:source_id>/')
def source_view(source_id):
  articles = get_articles_based_on_source(source_id)
  sources = get_sources()
  print(articles)
  current_source = None
  for source in sources:
    if source["id"] == source_id:
      current_source = source
  return render_template('pages/sourceview.html', current_source=current_source, sources=sources, articles=articles)

# @main.route('/general/')
# def index():
#   sources = get_sources()
#   return render_template('pages/index.html', sources=sources)