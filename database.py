from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.types as types

class Timestamp(types.TypeDecorator):
    impl = types.Integer
    
    def process_bind_param(self, value, dialect):
        return int(value.timestamp() * 1000)

    def process_result_value(self, value, dialect):
        return datetime.fromtimestamp(value / 1000)


db = SQLAlchemy()
