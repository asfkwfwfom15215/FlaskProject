from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html") # index.html 파일 렌더링


@app.route('/버튼_클릭_동작')
def button_action():
    return "버튼이 클릭됐습니다!" # 버튼 클릭 시 이 문구 출력


if __name__ == '__main__':
    app.run(debug=True)

