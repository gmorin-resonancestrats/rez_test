from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>🚀 Mon Application Flask sur Railway!</h1>
    <p>Bravo! Votre application fonctionne correctement.</p>
    """

@app.route('/test')
def test():
    return {"status": "success", "message": "L'API fonctionne!"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)