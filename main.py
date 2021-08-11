"""
This is the main module of the API
"""
from routes import routes
from config import app

@app.route('/')
def helloworld():
    """
    This is a test endpoint to verify if the basic structure of the app is running correctly
    """
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
