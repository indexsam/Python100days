from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(1000), nullable=False)

    

with app.app_context():
    db.create_all()

 # CREATE THE FORM
class MovieFormUpdate(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('update')   

class MovieFormAdd(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')  

# Defining the API
URL="https://api.themoviedb.org/3/search/movie"
URL2= "https://api.themoviedb.org/3/movie/"


headers = {
  "Authorization": f"Bearer {os.getenv('KEY')}",
  "accept": "application/json",
}

Image_source="https://image.tmdb.org/t/p/w500"
 
# title  (user input)
# year *
# description *
# rating *
# ranking
# review
# img_url *    

# @app.route("/add", methods=["GET","POST"])
# def add():

#     if request.method == "POST":
      
#         # CREATE RECORD
#         with app.app_context():
#             new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
#             db.session.add(new_book)
#             db.session.commit()
#             print(new_book)
#         return redirect(url_for('home'))
#     return render_template("add.html")
'''
curl --request GET \
     --url 'https://api.themoviedb.org/3/search/movie?query=the%20matrix&include_adult=false&language=en-US&page=1' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2E5MzY0NjRlNjJhMTRkYWRiNjA3YjMxNDY4Mzg1ZCIsIm5iZiI6MTcyMzIyNjY3OS44ODk4NjcsInN1YiI6IjY2YjY1NjcxN2Y4ODBlY2NjOTllYmRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mBvN21UhmQ2PsfAGp4uEdX6RwsMgCUAiJzOcdV0r1J4' \
     --header 'accept: application/json'

curl --request GET \
     --url 'https://api.themoviedb.org/3/movie/603?language=en-US' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2E5MzY0NjRlNjJhMTRkYWRiNjA3YjMxNDY4Mzg1ZCIsIm5iZiI6MTcyMzIyNjY3OS44ODk4NjcsInN1YiI6IjY2YjY1NjcxN2Y4ODBlY2NjOTllYmRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mBvN21UhmQ2PsfAGp4uEdX6RwsMgCUAiJzOcdV0r1J4' \
     --header 'accept: application/json'
'''
@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars() # .all() 
    return render_template("index.html", movies=all_movies)

@app.route("/update/<int:id>")
def update_form(id):
    form = MovieFormUpdate()
    return render_template("edit.html", id=id, form=form)

@app.route("/update/<int:id>", methods=["POST"])
def update_action(id):
    form = MovieFormUpdate()
    if form.validate_on_submit():
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit() 
    return redirect(url_for('home'))
    
@app.route("/delete/<int:id>")
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add")
def addForm():
    form=MovieFormAdd()
    return render_template("add.html", form=form)


@app.route("/add", methods=["POST"])
def addForm_action():
    form = MovieFormAdd()
    if form.validate_on_submit():

        parameters = {
        "query":f"{form.title.data}",
        "include_adult": "false",
        "language": "en-US",
        "page": 1,
        }
        response = requests.get(URL, params=parameters, headers=headers)
        response.raise_for_status()
        data=response.json()
        
    return render_template("select.html", data=data["results"] )

@app.route("/add/<int:id>", methods=["GET"])
def addForm_action2(id):
           
        parameters = {
          "language": "en-US",
        }

        response = requests.get(URL2+str(id), params=parameters, headers=headers)
        response.raise_for_status()
        data=response.json()
        # print(data)
        # CREATE RECORD
        with app.app_context():
            new_movie = Movie(title=data["title"], img_url= (Image_source + data["poster_path"]), \
                              year=data["release_date"][:4], description=data["overview"], \
                                  ranking=0, review="", rating=0.0)
            db.session.add(new_movie)
            db.session.commit()
        latest_movie = db.session.execute(db.select(Movie).order_by(desc(Movie.id))).scalars().first()
        return redirect(url_for('update_form', id=latest_movie.id))
        
        
        



if __name__ == '__main__':
    app.run(debug=True)
