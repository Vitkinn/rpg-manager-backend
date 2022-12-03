from sql_alchemy import database
from sqlalchemy.sql.expression import func
from datetime import date

class SheetModel (database.Model):

    __tablename__ = 'character_sheet'
    id_sheet = database.Column(database.Integer, primary_key = True)
    ds_level_class = database.Column(database.String(50))
    dt_creation = database.Column(database.Date)
    dt_update = database.Column(database.Date)
    nm_antecedent = database.Column(database.String(50))
    nm_character = database.Column(database.String(255))
    nm_race = database.Column(database.String(50))
    nr_armor_class = database.Column(database.Integer)
    nr_bonus_proficiency = database.Column(database.Integer)
    nr_charisma = database.Column(database.Integer)
    nr_constitution = database.Column(database.Integer)
    nr_dexterity = database.Column(database.Integer)
    nr_displacement = database.Column(database.Integer)
    nr_experience = database.Column(database.Integer)
    nr_force = database.Column(database.Integer)
    nr_initiative = database.Column(database.Integer)
    nr_inspiration = database.Column(database.Integer)
    nr_intelligence = database.Column(database.Integer)
    nr_wisdom = database.Column(database.Integer)

    dt_creation = date.today()

    def __init__(self, id_sheet, ds_level_class, nm_antecedent, nm_character, nm_race, nr_armor_class,
                 nr_bonus_proficiency, nr_charisma, nr_constitution, nr_dexterity, nr_displacement,
                 nr_experience, nr_force, nr_initiative, nr_inspiration, nr_intelligence, nr_wisdom):
        self.id_sheet = id_sheet
        self.ds_level_class = ds_level_class
        self.dt_update = date.today()
        self.nm_antecedent = nm_antecedent
        self.nm_character = nm_character
        self.nm_race = nm_race
        self.nr_armor_class = nr_armor_class
        self.nr_bonus_proficiency = nr_bonus_proficiency
        self.nr_charisma = nr_charisma
        self.nr_constitution = nr_constitution
        self.nr_dexterity = nr_dexterity
        self.nr_displacement = nr_displacement
        self.nr_experience = nr_experience
        self.nr_force = nr_force
        self.nr_initiative = nr_initiative
        self.nr_inspiration = nr_inspiration
        self.nr_intelligence = nr_intelligence
        self.nr_wisdom = nr_wisdom

    def json(self):
        return {
            'id_sheet' : self.id_sheet,
            'ds_level_class' : self.ds_level_class,
            'dt_update' : self.dt_update,
            'nm_antecedent' : self.nm_antecedent,
            'nm_character' : self.nm_character,
            'nm_race' : self.nm_race,
            'nr_armor_class' : self.nr_armor_class,
            'nr_bonus_proficiency' : self.nr_bonus_proficiency,
            'nr_charisma' : self.nr_charisma,
            'nr_constitution' : self.nr_constitution,
            'nr_dexterity' : self.nr_dexterity,
            'nr_displacement' : self.nr_displacement,
            'nr_experience' : self.nr_experience,
            'nr_force' : self.nr_force,
            'nr_initiative' : self.nr_initiative,
            'nr_inspiration' : self.nr_inspiration,
            'nr_intelligence' : self.nr_intelligence,
            'nr_wisdom' : self.nr_wisdom
            }

    @classmethod
    def find_sheet_by_id(cls, id_sheet): 
        sheet = cls.query.filter_by(id_sheet = id_sheet).first()
        if sheet:
            return sheet
        return None

    @classmethod
    def find_sheet_by_name(cls, nm_character): 
        sheet = cls.query.filter_by(nm_character = nm_character).first()
        if sheet:
            return sheet
        return None

    def save_sheet(self): 
        database.session.add(self)
        database.session.commit()

    def update_sheet(self, id_sheet, ds_level_class, nm_antecedent, nm_character, nm_race, nr_armor_class,
                 nr_bonus_proficiency, nr_charisma, nr_constitution, nr_dexterity, nr_displacement,
                 nr_experience, nr_force, nr_initiative, nr_inspiration, nr_intelligence, nr_wisdom): 
        self.id_sheet = id_sheet
        self.ds_level_class = ds_level_class
        self.dt_update = date.today()
        self.nm_antecedent = nm_antecedent
        self.nm_character = nm_character
        self.nm_race = nm_race
        self.nr_armor_class = nr_armor_class
        self.nr_bonus_proficiency = nr_bonus_proficiency
        self.nr_charisma = nr_charisma
        self.nr_constitution = nr_constitution
        self.nr_dexterity = nr_dexterity
        self.nr_displacement = nr_displacement
        self.nr_experience = nr_experience
        self.nr_force = nr_force
        self.nr_initiative = nr_initiative
        self.nr_inspiration = nr_inspiration
        self.nr_intelligence = nr_intelligence
        self.nr_wisdom = nr_wisdom

    def delete_sheet(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_last_sheet(cls):
        id_sheet = database.session.query(func.max(cls.id_sheet)).one()[0]

        if id_sheet:
            return id_sheet + 1
        return 1
