from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
import time

app = Flask(__name__) 
cred = credentials.Certificate('Key.json')   
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-dormitory-door-default-rtdb.firebaseio.com/'   
})

@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/save_to_firebase', methods=['POST'])
def save_to_firebase():
    ref = db.reference('On')
    ref.set(1)
    time.sleep(1)
    ref.set(0)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)