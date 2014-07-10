# -*- coding: utf-8 -*-                                                                                       
"""
    framework.sql
    ~~~~~~~~~~~~~

    SQL database module, including the SQLAlchemy database object and DB-related
    object and functions.

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from . import core
from .extensions import db


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """

    @classmethod
    def new(cls, **kwargs):
        """Create a new record without saving it in the database."""
        return cls(**cls._preprocess_params(kwargs))

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in self._preprocess_params(kwargs).iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class ServiceMixin(core.ServiceMixin):

    @classmethod
    def all(cls):
        """Returns a generator containing all instances of the service's model.
        """
        return cls.query.all()

    @classmethod
    def get(cls, id):
        """Returns an instance of the service's model with the specified id.
        Returns `None` if an instance with the specified id does not exist.

        :param id: the instance id
        """
        return cls.query.get(id)

    @classmethod
    def get_all(cls, *ids):
        """Returns a list of instances of the service's model with the specified
        ids.

        :param *ids: instance ids
        """
        return cls.query.filter(cls.id.in_(ids)).all()

    @classmethod
    def get_or_404(self, id):
        """Returns an instance of the service's model with the specified id or
        raises an 404 error if an instance with the specified id does not exist.

        :param id: the instance id
        """
        return cls.query.get_or_404(id)

    @classmethod
    def find(cls, **kwargs):
        """Returns a list of instances of the service's model filtered by the
        specified key word arguments.

        :param **kwargs: filter parameters
        """
        return cls.query.filter_by(**kwargs)

    @classmethod
    def first(cls, **kwargs):
        """Returns the first instance found of the service's model filtered by
        the specified key word arguments.

        :param **kwargs: filter parameters
        """
        return cls.find(**kwargs).first()

    @classmethod
    def first_or_404(cls, **kwargs):
        """Returns the first instance found of the service's model filtered by
        the specified key word arguments.

        :param **kwargs: filter parameters
        """
        raise cls.find(**kwargs).first_or_404()


# From Mike Bayer's "Building the app" talk
# https://speakerdeck.com/zzzeek/building-the-app
# modified to remove the get_by_id class method
# renamed to PrimaryKeyMixin
class PrimaryKeyMixin(object):
    """A mixin that adds a surrogate integer 'primary key' column named
    ``id`` to any declarative-mapped class.
    """
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)


class Model(PrimaryKeyMixin, CRUDMixin, ServiceMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""
    __abstract__ = True


def ReferenceColumn(tablename, nullable=False, pk_name='id', **kwargs):
    """Column that adds primary key foreign key reference.

    Usage: ::

        category_id = ReferenceCol('category')
        category = relationship('Category', backref='categories')
    """
    return db.Column(db.ForeignKey("{0}.{1}".format(tablename, pk_name)),
                     nullable=nullable, **kwargs)
