from flask import Flask
from subprocess import Popen,PIPE
import os

app = Flask(__name__)

@app.route("/")
def root():
    return "Root_hit"

@app.route("/app1")
def app1():
    process = Popen(['hostname'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    stdout=str(stdout.decode())
    return f"app1_hit from ----------->>> {stdout}"

@app.route("/app2")
def app2():
    process = Popen(['hostname'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    stdout=str(stdout.decode())
    return f"app2_hit from ----------->>> {stdout}"

print(os.getppid())
print(os.getpid())

app.run(host='0.0.0.0')


