from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
import sqlite3

'''
Code Here
'''

app = Flask(__name__)
Bootstrap5(app)

all_books = []
db = sqlite3.connect("./books-collection.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books \
                (id INTEGER PRIMARY KEY, \
                title varchar(250) NOT NULL UNIQUE, \
               author varchar(250) NOT NULL, \
                rating FLOAT NOT NULL)")

cursor.execute("Delete from books")
db.commit()
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

@app.route('/')
def home():

    return render_template("index.html", books=all_books)



@app.route("/add", methods=["GET","POST"])
def add():

    if request.method == "POST":
        all_books.append(
            {
                "title": request.form["title"],
                "author": request.form["author"],
                "rating": request.form["rating"],
            }
        )
        print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

