app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Poliscope'
db = SQLAlchemy(app)
app.config.update(
    DEBUG = True,
)
