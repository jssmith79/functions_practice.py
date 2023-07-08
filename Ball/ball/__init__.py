
from flask import Flask 
def create_app(): 
    app = Flask(__name__)


#complete later with DB config

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Rusty123-@localhost:5432/ballpy'
    app.config['SQLALCHEM_TRACK_MODIFICATIONS'] = False


    from . import models
    from flask_migrate import Migrate
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    from . import reptile
    app.register_blueprint(reptile.bp)

    @app.route('/')
    def main():
        return 'This is the Ball API.'
    
    return app