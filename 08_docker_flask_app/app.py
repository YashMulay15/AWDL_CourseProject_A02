from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Docker Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f4f8;
                    text-align: center;
                    padding-top: 80px;
                }
                .box {
                    background: white;
                    width: 500px;
                    margin: auto;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px gray;
                }
                h1 {
                    color: #007bff;
                }
                p {
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Dockerized Flask Application</h1>
                <p>This Flask application is running inside a Docker container.</p>
                <p>Status: Running Successfully</p>
            </div>
        </body>
    </html>
    """

@app.route("/api/status")
def status():
    return jsonify({
        "application": "Docker Flask App",
        "status": "running",
        "message": "Flask app is running successfully inside Docker container"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)