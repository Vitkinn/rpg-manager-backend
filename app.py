from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.users import User, UserLogin
from resources.tables import Table

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

DATABASE_URI = 'mysql+pymysql://root:admin@localhost/rpg?charset=utf8mb4' # Modify this URL.
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Senai2022'

@app.before_first_request
def create_database():
    database.create_all()

api.add_resource(User, '/users/<int:id_user>')
api.add_resource(UserLogin, '/login')
api.add_resource(Table, '/table/<int:id_table>')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
