
app = Flask(__name__)
assets = flask_assets.Environment()
assets.init_app(app)