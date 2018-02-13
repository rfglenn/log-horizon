from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref



Base = declarative_base()

interval_tags = Table('interval_tags', Base.metadata,
	Column('tag_id', Integer, ForeignKey('tags.id')),
	Column('interval_id', Integer, ForeignKey('intervals.id'))
)


class Interval(Base):
	__tablename__ = 'intervals'
	
	id = Column(Integer, primary_key=True)
	started = Column(DateTime)
	ended =  Column(DateTime)
	description = Column(String)
	tags = relationship('Tag', secondary = interval_tags, backref = backref('intervals', lazy='dynamic'))

	def __repr__(self):
		str_started = self.started.strftime("%Y-%m-%d %H:%M:%S")
		str_ended = self.ended.strftime("%Y-%m-%d %H:%M:%S")
		return "<Interval from %s to %s>" % (str_started, str_ended)

class Tag(Base):

    __tablename__ = 'tags'

    id      =   Column(Integer, primary_key=True)
    name    =   Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % (self.name)
