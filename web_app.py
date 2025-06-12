from main import app
import os

# Get the PORT from environment variable
port = int(os.environ.get("PORT", 8000))

# The app variable will be used by Gunicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web_app:app", host="0.0.0.0", port=port, log_level="info")
