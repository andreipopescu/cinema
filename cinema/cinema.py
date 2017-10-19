from flask import Flask, render_template # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
# app.config.from_envvar('CINEMA_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('')
