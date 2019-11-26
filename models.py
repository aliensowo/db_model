from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstarct__ = True

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)


class GeoModels(Base):
    geo = db.Column('geo', db.String, nullable=False)


class PostRatingModels(Base):
    post_rating = db.Column('rating', db.String, default=0)


class PostPhotoModels(Base):
    post_photo = db.Column('photo', db.String, nullable=False)


class Auths(Base):
    to_user_id = db.Column('to_user_id', db.Integer, db.ForeignKey('profiles.id'))
    password = db.Column('password', db.String, nullable=False)
    login = db.Column('login', db.String, nullable=False)


class Profiles(Base):
    first_name = db.Column('first_name', db.String(45), nullable=False)
    second_name = db.Column('second_name', db.String(45), nullable=False)
    profile_rating = db.Column('profile_rating', db.Double(10), nullable=False)
    profile_photo = db.Column('profile_photo', db.String, nullable=False)


class PostInProfiles(Base):
    id_user = db.Column('user_id', db.Integer, db.ForeignKey('profiles.id'))
    id_geo = db.Column('geo', db.String, db.ForeignKey('geomodels.id'))
    id_rating = db.Column('rating', db.Double, db.ForeignKey('postratingmodels.id'))
    id_in_p_post_photo = db.Column('post_photo', db.String, db.ForeignKey('postphotomodels.id'))
    day_of_creating = db.Column('day', db.Date, nullable=False)
    date = db.Column('date_time', db.Datetime, nullable=False)


class PostInSpaces(Base):
    id_user = db.Column('id_user', db.Integer, db.ForeignKey('profiles.id'))
    id_rating = db.Column('rating', db.Double, db.ForeignKey('postratingmodels.id'))
    id_in_s_post_photo = db.Column('post_photo', db.String, db.ForeignKey('postphotomodels.id'))


