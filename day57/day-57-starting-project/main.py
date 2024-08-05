from flask import Flask, render_template
from post import Post

app = Flask(__name__)


posts = Post.get_url()

@app.route('/')
def home():
    return render_template("index.html", postdata=posts)

@app.route('/blog/<int:id>')
def blogpost(id):
    targetblog=None
    for blog in posts:
        if blog["id"]==id:
            targetblog = blog

    return render_template("post.html", post=targetblog)

if __name__ == "__main__":
    app.run(debug=True)
