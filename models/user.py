from sql_alchemy import database
from sqlalchemy.sql.expression import func
from datetime import date

class UserModel (database.Model):

    __tablename__ = 'user'
    id_user = database.Column(database.Integer, primary_key = True)
    ie_type = database.Column(database.Integer)
    ds_avatar = database.Column(database.String(255))
    ds_email = database.Column(database.String(255))
    ds_name = database.Column(database.String(255))
    ds_password = database.Column(database.String(50))
    dt_creation = database.Column(database.Date)
    dt_update = database.Column(database.Date)
    nm_user = database.Column(database.String(50))
    nr_contact = database.Column(database.Integer)

    table = database.relationship('TableModel', backref='user_table', primaryjoin='UserModel.id_user==TableModel.user_id', lazy='dynamic')

    def __init__(self, id_user, ds_email, nm_user, ds_name,
                 ds_password, nr_contact):
        self.id_user = id_user
        self.ie_type = 1
        self.ds_avatar = "C:"
        self.ds_email = ds_email
        self.ds_name = ds_name
        self.ds_password = ds_password
        self.dt_creation = date.today()
        self.dt_update = date.today()
        self.nr_contact = nr_contact
        self.nm_user = nm_user

    def json(self):
        return {
            'id_user' : self.id_user,
            'ie_type' : self.ie_type,
            'ds_avatar' : self.ds_avatar,
            'ds_email' : self.ds_email,
            'ds_name' : self.ds_name,
            'ds_password': self.ds_password,
            'dt_creation' : str(self.dt_creation),
            'dt_update' : str(self.dt_update),
            'nm_user' : self.nm_user,
            'nr_contact' : self.nr_contact
            }

    @classmethod
    def find_user_by_id(cls, id_user): 
        user = cls.query.filter_by(id_user = id_user).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_by_login(cls, nm_user): 
        user = cls.query.filter_by(nm_user = nm_user).first()
        if user:
            return user
        return None

    def save_user(self): 
        database.session.add(self)
        database.session.commit()

    def update_user(self, id_user, nm_user, password): 
        self.id_user = id_user
        self.nm_user = nm_user
        self.password = password

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_last_user(cls):
        id_user = database.session.query(func.max(cls.id_user)).one()[0]

        if id_user:
            return id_user + 1
        return 1
