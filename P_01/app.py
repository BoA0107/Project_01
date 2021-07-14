from flask import *
from F_SQL import *

app = Flask(__name__)


@app.route('/')
def SQL():
    return render_template("SQL.html", Batch=Batch, deploy=deploy,ShouDao=ShouDao,other=other)


if __name__ == '__main__':
    app.run(debug=True)
