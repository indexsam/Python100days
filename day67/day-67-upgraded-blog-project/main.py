from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)




with app.app_context():
    db.create_all()


# CREATE THE FORM
class BlogForm(FlaskForm):
    title = StringField('Blog post title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit post') 

@app.route('/')
def get_all_posts():
   
    posts = []
    posts=db.session.execute(db.select(BlogPost)).scalars().all()
    
    return render_template("index.html", all_posts=posts)


@app.route('/showpost/<int:post_id>')
def show_post(post_id):
    
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post   
@app.route('/new-post', methods=["GET","POST"])
def newPost():
    form = BlogForm()
    edit_mode=False
    if form.validate_on_submit():
        with app.app_context():
            post = BlogPost(title=request.form.get("title"), subtitle=request.form.get("subtitle"),\
                         body=request.form.get("body"), img_url=request.form.get("img_url"),\
                             date = datetime.now().strftime("%B %d, %Y"), author=request.form.get("author") )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, edit=edit_mode)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:id>', methods=["GET","POST"])
def editPost(id):
 
    edit_mode=True
    post = db.get_or_404(BlogPost, id)
    form = BlogForm(
                title=post.title,
                subtitle=post.subtitle,
                img_url=post.img_url,
                author=post.author,
                body=post.body 
                                )
    if form.validate_on_submit():
        
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.img_url = form.img_url.data
            post.author = form.author.data
            post.body = form.body.data    
            db.session.commit()

            return redirect(url_for("show_post", post_id=post.id))
    
    return render_template("make-post.html", form=form, edit=edit_mode)
    
# TODO: delete_post() to remove a blog post from the database
@app.route('/delete-post/<int:id>', methods=["GET","POST"])
def deletePost(id):
        with app.app_context():
            blog_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == id)).scalar()
            db.session.delete(blog_to_delete)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
 
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
