'''
TPNG: JoY
ROSTER: Yuki Feng, Joshua Liu
QCC:

'''

from Flask import Flask

app = Flask(__name__)

@app.route("/main")
def index():
    return render_template()

if __name__ == "__main__":
    app.debug = True
    app.run()
