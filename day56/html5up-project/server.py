from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)

# document.body.contentEditable=true  (browser console hint) 

# unsplash.com for background templates

#  https://www.freeconvert.com/ico-converter (convert png to ico)