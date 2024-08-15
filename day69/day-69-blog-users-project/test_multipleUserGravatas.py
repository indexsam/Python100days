import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    custom_avatar_url = db.Column(db.String(255), nullable=True)  # Custom avatar URL field


def get_gravatar_url(user, size=100, default=None):
    # Use the user's custom avatar URL if available
    if user.custom_avatar_url:
        return user.custom_avatar_url

    # If no custom avatar, use Gravatar
    email_hash = hashlib.md5(user.email.lower().encode('utf-8')).hexdigest()
    if default is None:
        default = 'https://example.com/default-avatar.png'  # Replace with your default image URL
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default}"


@app.route('/users')
def users():
    # Get all users from the database
    users = User.query.all()
    
    # Create a list of dictionaries with user info and avatar URLs
    user_data = [{
        'id': user.id,
        'email': user.email,
        'avatar_url': get_gravatar_url(user) # to return the url in the database. 
    } for user in users]
    
    # Pass the data to the template
    return render_template('users.html', users=user_data)


