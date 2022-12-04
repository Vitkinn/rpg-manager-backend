from sql_alchemy import database
from sqlalchemy.sql.expression import func
from datetime import date

from models.table import TableModel

class MapModel (database.Model):

    __tablename__ = 'r_map'
    id_r_map = database.Column(database.Integer, primary_key = True)
    ds_map_image = database.Column(database.String(255))
    dt_upload = database.Column(database.Date)
    table_id = database.Column(database.Integer, database.ForeignKey(TableModel.id_table), primary_key=True)

    table = database.relationship(TableModel, foreign_keys='MapModel.table_id')

    def __init__(self, id_r_map, table_id, ds_map_image):
        self.id_r_map = id_r_map
        self.ds_map_image = ds_map_image
        self.dt_creation = date.today()
        self.table_id = table_id

    def json(self):
        return {
            'id_r_map' : self.id_r_map,
            'ds_map_image' : self.ds_map_image,
            'dt_creation' : self.dt_creation,
            'table_id' : self.table_id
            }

    @classmethod
    def find_map_by_id(cls, id_r_map): 
        map = cls.query.filter_by(id_r_map = id_r_map).first()
        if map:
            return map
        return None

    @classmethod
    def find_map_by_ds_map(cls, ds_map_image): 
        map = cls.query.filter_by(ds_map_image = ds_map_image).first()
        if ds_map_image:
            return ds_map_image
        return None

    def save_map(self): 
        database.session.add(self)
        database.session.commit()

    def update_map(self, id_r_map, table_id, ds_map_image):
        self.id_r_map = id_r_map
        self.ds_map_image = ds_map_image
        self.dt_creation = date.today()
        self.table_id = table_id

    def delete_map(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_last_map(cls):
        id_r_map = database.session.query(func.max(cls.id_r_map)).one()[0]

        if id_r_map:
            return id_r_map + 1
        return 1
