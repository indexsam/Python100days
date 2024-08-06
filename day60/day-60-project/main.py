from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
response.raise_for_status()
posts = response.json()

app = Flask(__name__)

my_email = "obxxxindexxxm@gmail.com"
password = "xxxxxxxxxxxxx"

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="obadansam@gmail.com",
                    msg=f"Subject: Customer details!!\n\n{message}")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        email_message= name + "\n" + email + "\n" + phone + "\n" + message 
        send_mail(email_message)
        return render_template("contact.html", msg="Successfully sent message")


    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
