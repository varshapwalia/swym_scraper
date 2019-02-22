import sys
from flask import Flask, Blueprint, redirect, current_app, request, session, g, abort, render_template, Response

from helper import *

scraper = Blueprint('scraper', __name__)

@scraper.route('/web_search', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    try:

      search = request.form['search']
      products = search_weburl(search)

      return render_template("scraper/search.html",products=products,query=search)
    except Exception as e:
      print e
      return Response("Something Went Wrong")
  if request.method == 'GET':
    result = {'total':0, 'within_24hrs':0, '24hrs_to_7days':0,'beyond_7days':0}
    return render_template("scraper/search.html",result=result)
  