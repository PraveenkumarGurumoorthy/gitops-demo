from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>GitOps Demo Application</h1>
    <h2>Welcome!</h2>
    <p>Deployment: Successful</p>
    <p>Powered by Docker, Kubernetes and Argo CD</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "gitops-demo",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)