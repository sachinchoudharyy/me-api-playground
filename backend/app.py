import os
from flask import Flask
from flask_cors import CORS
from routes import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets port dynamically
    app.run(host="0.0.0.0", port=port)
