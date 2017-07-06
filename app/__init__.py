from flask import Flask

print 'name: ' + __name__
app = Flask(__name__)
from app import views
