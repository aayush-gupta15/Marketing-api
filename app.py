from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.user import UserRegister, User
from resources.facebook import Facebook, FacebookCampaignList
from config import postgresqlConfig

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"  # temp JWT!
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user')
api.add_resource(Facebook, '/store/<string:name>')
api.add_resource(FacebookCampaignList, '/stores')

if __name__ == '__main__':
    app.run(debug=True)