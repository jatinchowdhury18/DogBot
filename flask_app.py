from flask import Flask
import atexit
from apscheduler.schedulers.blocking import BlockingScheduler
import send_sms

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello again (from Flask!)'

def server():
    send_sms.main()

job_defaults = {
    'coalesce': False,
    'max_instances': 5
}
cron = BlockingScheduler (job_defaults=job_defaults, daemon=True)
cron.add_job (server, 'interval', minutes=154)
cron.start()

atexit.register (lambda: cron.shutdown (wait=False))


if __name__ == "__main__":
    app.run(debug=True)
