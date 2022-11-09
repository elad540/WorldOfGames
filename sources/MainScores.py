from flask import Flask, render_template
from utils import scores_file_name
from Score import get_current_score


app = Flask(__name__, template_folder='template')


@app.route('/')
def content():
    if type(scores_file_name) != int:
        score = get_current_score
        error = ""
        return render_template('error.html', error=error)
    else:
        score = f"The score is {scores_file_name}"
        error = ""
    return render_template('index.html', score=score, error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=30000)
