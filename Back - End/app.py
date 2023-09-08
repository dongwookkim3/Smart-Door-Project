from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
import time

app = Flask(__name__)

# Firebase 초기화
cred = credentials.Certificate('Key.json')  # 서비스 계정 키의 경로
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-dormitory-door-default-rtdb.firebaseio.com/'  # Firebase 프로젝트의 데이터베이스 URL
})

# 루트 경로에 HTML 템플릿을 렌더링합니다.
@app.route('/')
def index():
    return render_template('index.html')

# 버튼을 클릭하면 Firebase에 1을 저장하고 3초 동안 대기합니다.
@app.route('/save_to_firebase', methods=['POST'])
def save_to_firebase():
    ref = db.reference('On')
    ref.set(1)
    time.sleep(3)
    ref.set(0)  # 3초 후에 값을 다시 None으로 설정하여 초기화
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
