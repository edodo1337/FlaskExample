from app import app
from flask import render_template

from models import Post

@app.route('/')
def index():
    name = 'mike'
    posts = Post.query.all()
    return render_template('index.html', name=name, posts=posts)