from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "CS321 Database CI Test"

@app.route("/health")
def health():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "cs321"),
            user=os.getenv("DB_USER", "cs321"),
            password=os.getenv("DB_PASSWORD", "cs321")
        )

        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()

        cur.close()
        conn.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
