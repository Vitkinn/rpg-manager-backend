from sql_alchemy import database
from sqlalchemy.sql.expression import func
from datetime import date

from models.table import TableModel

class MapModel (database.Model):

    __tablename__ = 'r_map'
    id_r_map = database.Column(database.Integer, primary_key = True)
    table_id = database.Column(database.Integer, database.ForeignKey(TableModel.id_table), primary_key=True)
    ds_map_image = database.Column(database.String(255))

    table = database.relationship(TableModel, foreign_keys='MapModel.table_id')

    def __init__(self, id_r_map):
        self.id_r_map = id_r_map

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
