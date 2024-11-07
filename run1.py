from main1 import app
import uvicorn

if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run("main1:app", host="127.0.0.1", port=8000, reload=True)
