import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


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


def rotate_questions():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Fetch all regions and their cycle configurations
        cursor.execute("SELECT * FROM cycle_config")
        configs = cursor.fetchall()

        for config in configs:
            region = config['region']
            cycle_duration = config['cycle_duration']
            start_time = config['start_time']

            # Check if we need to rotate the question based on duration
            cursor.execute("SELECT * FROM current_cycle WHERE region = %s", (region,))
            current_cycle_info = cursor.fetchone()

            if current_cycle_info:
                current_cycle = current_cycle_info['current_cycle']
                last_update = current_cycle_info['last_update']
                next_rotation_time = last_update + timedelta(days=cycle_duration)

                # If it's time to rotate
                if datetime.now() >= next_rotation_time:
                    new_cycle = current_cycle + 1

                    # Update to the next cycle
                    cursor.execute(
                        "UPDATE current_cycle SET current_cycle = %s, last_update = NOW() WHERE region = %s",
                        (new_cycle, region)
                    )
                    conn.commit()
                    print(f"Rotated to cycle {new_cycle} for region {region}.")
            else:
                print(f"No current cycle info for region {region}.")

    except Exception as e:
        print(f"Error rotating questions: {str(e)}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    rotate_questions()
