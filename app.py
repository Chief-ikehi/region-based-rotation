from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)


# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conn


# Get the current question for a specific region
@app.route('/api/v1/question/<region>', methods=['GET'])
def get_current_question(region):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Fetch the current cycle info
        cursor.execute("SELECT current_cycle FROM current_cycle WHERE region = %s", (region,))
        cycle_info = cursor.fetchone()

        if cycle_info is None:
            return jsonify({"error": "Region not found"}), 404

        # Get the current cycle question
        current_cycle = cycle_info['current_cycle']
        cursor.execute("SELECT question_text FROM questions WHERE id = %s AND region = %s", (current_cycle, region))
        question = cursor.fetchone()

        if question:
            return jsonify({"region": region, "question": question['question_text']}), 200
        else:
            return jsonify({"error": "Question not found for this cycle"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)