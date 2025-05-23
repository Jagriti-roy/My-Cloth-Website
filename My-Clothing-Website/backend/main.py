from flask_cors import CORS
from flask import Flask,render_template,request,jsonify,send_from_directory,send_file
from flask_jwt_extended import JWTManager
from flask import Flask
from config import DevelopmentConfig
from application.models import db
from application.sec import cache
from application.worker import *
from application.tasks import *
from celery.result import AsyncResult
from celery.schedules import crontab
from celery import shared_task

#####################################################################################################################################################


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    db.init_app(app)
    cache.init_app(app)

    jwt = JWTManager(app)

    with app.app_context():
        import application.views

    return app

app = create_app()
celery_app=celery_init_app(app)

#############################################################      This is the Coding Section       ################################################
##################################################################################################################################################
#################################################################       CELERY TASKS       ######################################################

@app.get('/download-csv')
def download_csv():
    task = create_service_req_csv.delay()
    return jsonify({"task-id":task.id})

@app.get('/get-csv/<string:task_id>')
def get_csv(task_id):
    res = AsyncResult(task_id)
    if res.ready():
        filename = res.result
        return send_file(filename,as_attachment=True)
    else:
        return jsonify({"Message":"Task-Pending"}) , 404

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab( hour=0, minute=20),
        daily_remainder.s('DAILY REMAINDER'),
    )

@celery_app.on_after_configure.connect
def setup_periodic_tasks_monthly(sender, **kwargs):
    sender.add_periodic_task(
        crontab( hour=0, minute=23),
        monthly_report.s('MONTHLT REPORT'),
    )


if __name__ == "__main__":
    app.run(debug = True)

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################