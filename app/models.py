from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


db.Model.metadata.reflect(bind=db.engine, schema='skiresorts')
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __table__=db.Model.metadata.tables['skiresorts.users']

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)

class SkiResort(db.Model):
    __table__=db.Model.metadata.tables['skiresorts.skiresorts_main']

    def __repr__(self):
        return 'Ski Resort: {}'.format(self.name)


class CurrencyType(db.Model):
    __table__=db.Model.metadata.tables['skiresorts.currency_type']

    def __repr__(self):
        return '<Currency: {}>'.format(self.currency)


class CategoryCountry(db.Model):
    __table__=db.Model.metadata.tables['skiresorts.category_country']

    def __repr__(self):
        return '<Category: {}>'.format(self.category) 


class Countries(db.Model):
    __table__=db.Model.metadata.tables['skiresorts.countries']

    def __repr__(self):
        return '<Country: {}>'.format(self.country)



