from app import db
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so


class User(db.Model):

    id           : so.Mapped[int]           = so.mapped_column(primary_key=True)
    username     : so.Mapped[str]           = so.mapped_column(sa.String(64), index=True, unique=True)
    email        : so.Mapped[str]           = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Property(db.Model):

    id              : so.Mapped[int]   = so.mapped_column(primary_key=True)
    name            : so.Mapped[str]   = so.mapped_column(sa.String(120), index= True, unique=True)
    address         : so.Mapped[str]   = so.mapped_column(sa.String(256), index=True)
    square_footage  : so.Mapped[float] = so.mapped_column()
    num_of_bedrooms : so.Mapped[int]   = so.mapped_column()
    num_of_bathrooms: so.Mapped[int]   = so.mapped_column()
    status          : so.Mapped[str]   = so.mapped_column(sa.String(64))

    def __repr__(self) -> str:
        return '<Property {}>'.format(self.name)
    
class House(db.Model):

    id               : so.Mapped[int] = so.mapped_column(primary_key=True)
    parking          : so.Mapped[str] = so.mapped_column(sa.String(64))
    private_pool     : so.Mapped[str] = so.mapped_column(sa.String(64))
    exterior_features: so.Mapped[str] = so.mapped_column(sa.String(64))

    def __repr__(self) -> str:
        return '<House>'

class Apartment(db.Model):

    id                   : so.Mapped[int] = so.mapped_column(primary_key=True)
    balcony              : so.Mapped[str] = so.mapped_column(sa.String(64))
    rentable_storage_unit: so.Mapped[str] = so.mapped_column(sa.String(64))
    fully_renovated_house: so.Mapped[str] = so.mapped_column(sa.String(64))

    def __repr__(self) -> str:
        return '<Apartment>'
