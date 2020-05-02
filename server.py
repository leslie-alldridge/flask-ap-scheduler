from flask import Flask
from flask_apscheduler import APScheduler
from time import sleep
from datetime import datetime
app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200


@app.route('/run-tasks')
def run_tasks():
    app.apscheduler.add_job(func=scheduled_task, trigger='interval', hours=24, id='my_job', next_run_time=datetime.now())
    return 'Scheduled several long running tasks.', 200


@app.route('/status')
def stats():
    print(app.apscheduler.get_jobs())

    return 'Scheduled several long running tasks.', 200

def scheduled_task():
    print('running script')
    sleep(10)
    print('script complete!!')
    app.apscheduler.remove_job('my_job')
    return True



app.run(host='0.0.0.0', port=5000)