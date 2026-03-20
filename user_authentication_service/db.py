#!/usr/bin/env python3
"""Provide database utilities for the authentication service."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """Manage database sessions and user persistence operations."""

    def __init__(self) -> None:
        """Initialize a new DB instance and reset the schema."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Return a memoized SQLAlchemy session bound to this engine."""
        if self.__session is None:
            db_session = sessionmaker(bind=self._engine)
            self.__session = db_session()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Create, persist, and return a new user."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Return the first user matching the provided query arguments.
        Raises NoResultFound if no user is found.
        Raises InvalidRequestError if invalid query arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise
        except Exception as e:
            from sqlalchemy.exc import InvalidRequestError
            if isinstance(e, InvalidRequestError):
                raise
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update attributes of a user identified by user_id."""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError()
            setattr(user, key, value)
        self._session.commit()
