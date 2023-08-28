from arkinventory import app, db

@app.route('/')
def home():
    return "Test"
