import os
from app import app, socketio

if __name__ == "__main__":
    # Use standard port 5000 for deployment
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host="0.0.0.0", port=port)
