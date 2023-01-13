from flask import Flask, render_template
from Score import get_current_score
from utils import bad_return_code

app = Flask(__name__, template_folder='template')


@app.route('/')
def content():
    if get_current_score == bad_return_code:
        error = "Couldn't read the score file"
        return render_template('error.html', error=error)
    else:
        score = get_current_score()
        error = ""
    return render_template('index.html', score=score, error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=30000)
