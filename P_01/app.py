from flask import *
from F_SQL import *
from F_home import *
from F_SQL import *
from F_deploy import *

app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template("home.html", links_dct=links_dct, plan_info=plan_info, others=others,
                           career_level=career_level)


@app.route('/SQL')
def SQL():
    return render_template("SQL.html", Batch=Batch, deploy_related=deploy_related, ShouDao=ShouDao, other=other)


@app.route('/deploy')
def deploy():
    return render_template("deploy.html", answer=answer, branch=branch)


@app.route('/project_01')
def project_01():
    return render_template(project_01)


if __name__ == '__main__':
    app.run(debug=True)
