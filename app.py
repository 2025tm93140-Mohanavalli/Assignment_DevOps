from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym",
        "status": "Application is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/workouts")
def workouts():
    return jsonify({
        "workouts": [
            {
                "name": "Strength Training",
                "duration": 60
            },
            {
                "name": "Cardio",
                "duration": 30
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)