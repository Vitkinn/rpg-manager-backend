from sql_alchemy import database
from sqlalchemy.sql.expression import func
from datetime import date

from models.user import UserModel

class TableModel (database.Model):

    __tablename__ = 'r_table'
    id_table = database.Column(database.Integer, primary_key = True)
    user_id = database.Column(database.Integer, database.ForeignKey(UserModel.id_user), primary_key=True)
    #character_id = database.Column(database.Integer, ForeignKey("character_sheet.id_sheet"))
    #r_map_id = database.Column(database.Integer, ForeignKey("r_map.id_map"))
    nm_table = database.Column(database.String(255))
    ds_table = database.Column(database.String(255))
    dt_creation = database.Column(database.Date)
    dt_update = database.Column(database.Date)
    
    user = database.relationship(UserModel, foreign_keys='TableModel.user_id')

    def __init__(self, id_table, user_id, nm_table, ds_table):
        self.id_table = id_table
        self.dt_creation = date.today()
        self.dt_update = date.today()
        self.user_id = user_id
        #self.character_id = character_id
        #self.r_map_id = r_map_id
        self.nm_table = nm_table
        self.ds_table = ds_table

    def json(self):
        return {
            'id_table' : self.id_table,
            'nm_table' : self.nm_table,
            'ds_table' : self.ds_table,
            'r_map_id' : self.r_map_id,
            #'user_id' : self.user_id,
            #'character_id' : self.character_id
            }

    @classmethod
    def find_table_by_id(cls, id_table): 
        table = cls.query.filter_by(id_table = id_table).first()
        if table:
            return table
        return None

    @classmethod
    def find_table_by_login(cls, nm_table): 
        table = cls.query.filter_by(nm_table = nm_table).first()
        if table:
            return table
        return None

    def save_table(self): 
        database.session.add(self)
        database.session.commit()

    def update_table(self, id_table, user_id, character_id, r_map_id, nm_table, ds_table):
        self.id_table = id_table
        self.user_id = user_id
        self.character_id = character_id
        self.r_map_id = r_map_id
        self.nm_table = nm_table
        self.ds_table = ds_table
        self.dt_update = date.today()

    def delete_table(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_last_table(cls):
        id_table = database.session.query(func.max(cls.id_table)).one()[0]

        if id_table:
            return id_table + 1
        return 1
