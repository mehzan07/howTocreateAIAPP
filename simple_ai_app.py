# Import the libraries
from flask import Flask, render_template, request
from textblob import TextBlob

# Create the Flask app
app = Flask(__name__, template_folder='templates')

# Define the home route
@app.route("/")
def home():
    # Render the home page template
    return render_template("home.html")

# Define the analyze route
@app.route("/analyze", methods=["POST"])
def analyze():
    # Get the text input from the user
    text = request.form["text"]
    # Create a TextBlob object from the text input
    blob = TextBlob(text)
    # Get the sentiment polarity of the text input
    polarity = blob.sentiment.polarity
    # Convert the polarity to a percentage
    percentage = round(polarity * 100, 2)
    # Render the analyze page template with the text and the percentage
    return render_template("analyze.html", text=text, percentage=percentage)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)