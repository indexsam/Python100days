from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():

    year = datetime.datetime.now().year
    return render_template("index.html", yr=year)

@app.route("/<name>")
def api_call(name):

    response=requests.get(f"https://api.genderize.io?name={name}")
    genderize = response.json()

    response2=requests.get(f"https://api.agify.io?name={name}")
    agify = response2.json()

    
    return render_template("api.html", person=genderize["name"].title(), sex=genderize["gender"], age=agify["age"])

@app.route("/blogs/<num>")
def blogpost(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogdata= response.json()
    return render_template("blogpost.html", data=blogdata, yr=num)



if __name__ == "__main__":
    app.run(debug=True)

# https://www.npoint.io/  fake blogs  website (good testing api)
