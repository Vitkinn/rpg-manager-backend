from sql_alchemy import database
from sqlalchemy.sql.expression import func

class UserModel (database.Model):

    __tablename__ = 'user'
    id_user = database.Column(database.Integer, primary_key = True)
    ie_type = database.Column(database.String(1))
    ds_avatar = database.Column(database.String(50))
    ds_email = database.Column(database.String(100))
    ds_login = database.Column(database.String(50))
    ds_name = database.Column(database.String(100))
    ds_password = database.Column(database.String(50))
    dt_creation = database.Column(database.Date)
    dt_update = database.Column(database.Date)
    nr_contact = database.Column(database.String(13))

    def __init__(self, id_user, ie_type, ds_avatar, ds_email, ds_login, ds_name,
                 ds_password, dt_creation, dt_update, nr_contact):
        self.id_user = id_user
        self.ie_type = ie_type
        ##self.ds_avatar = ds_avatar
        self.ds_email = ds_email
        self.ds_login = ds_login
        self.ds_name = ds_name
        self.ds_password = ds_password
        self.dt_creation = dt_creation
        self.dt_update = dt_update
        self.nr_contact = nr_contact

    def json(self):
        return {'id_user' : self.id_user,
        'login' : self.ds_login}

    @classmethod  
    def find_user_by_id(cls, id_user): 
        user = cls.query.filter_by(id_user = id_user).first()
        if user:
            return user
        return None

    @classmethod  
    def find_user_by_login(cls, ds_login): 
        user = cls.query.filter_by(ds_login = ds_login).first()
        if user:
            return user
        return None

    def save_user(self): 
        database.session.add(self)
        database.session.commit()

    def update_user(self, id_user, ds_login, password): 
        self.id_user = id_user
        self.ds_login = ds_login
        self.password = password

    def delete_user(self): 
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_last_user(cls):
        # id_user = database.engine.execute("select nextval('id_user') as new_id").fetchone() - postgres
        id_user = database.session.query(func.max(cls.id_user)).one()[0]

        if id_user:
            return id_user + 1
        return 1
