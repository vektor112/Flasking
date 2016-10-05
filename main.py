from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT', None))