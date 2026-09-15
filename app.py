from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CS 321 Azure Container Test</h1>
    <p>Version 1 deployed from GitHub.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
