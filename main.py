import os
from app.app import app

if __name__ == '__main__':
    try:
        port = int(os.getenv('PORT', 5000))
        app.run(debug=True, host='0.0.0.0', port=port)
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
