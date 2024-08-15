from flask import Flask, render_template
import hashlib

app = Flask(__name__)

# Function to generate Gravatar URL
def get_gravatar_url(email, size=50, default='retro'):
    # Create the MD5 hash of the email address
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    # Construct the Gravatar URL
     
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default}"

@app.route('/')
def index():
    # Example email address
    email = 'user@example.com'
    # Get the Gravatar URL
    gravatar_url = get_gravatar_url(email)
    # Pass the Gravatar URL to the template
    return render_template('gravater_test.html', gravatar_url=gravatar_url)

if __name__ == '__main__':
    app.run(debug=True)
