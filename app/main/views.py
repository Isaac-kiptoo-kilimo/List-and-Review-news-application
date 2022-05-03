from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles_based_on_source,process_articles


@main.route('/')
def index():
  sources = get_sources()
  return render_template('pages/index.html', sources=sources)


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