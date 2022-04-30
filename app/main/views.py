from flask import render_template,request,redirect,url_for
from . import main
from ..requests import *


@main.route('/')
def index():
  sources = get_sources()
  return render_template('pages/index.html', sources=sources)


@main.route('/sources/view/<string:source_id>/')
def source_view(source_id):
  sources = get_sources()
  return render_template('pages/index.html', sources=sources)