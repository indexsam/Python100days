from flask import Flask, render_template
import requests
import datetime

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
response.raise_for_status()
blogdata = response.json()

date_data = datetime.datetime.now().strftime('%B %d %Y')

app=Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=blogdata, datein=date_data)

@app.route('/about')
def about_us():
    return render_template("about.html")

@app.route('/contact')
def contact_us():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def mypost(id):
    targetpost=None
    for blog in blogdata:
        if blog["id"] == id:
            targetpost =blog

    return render_template("post.html", tblog=targetpost, datein=date_data)

if __name__=="__main__":
    app.run(debug=True)