import os
from flask import Flask, render_template
# from flask_mongoengine import MongoEngine
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

app.config.from_object('config.DevelopmentConfig')

# Connnect with mongodb
# Mongodb Settings are there in APP_SETTINGS
# db = MongoEngine(app)

# Importing Controllers
from controllers.main import main
from controllers.scraper import scraper

# Blueprint urls
app.register_blueprint(main)
app.register_blueprint(scraper)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)