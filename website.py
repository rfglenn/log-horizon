#stdlib
from datetime import datetime, timedelta

#external
from flask import Flask, Blueprint, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import iso8601
from sqlalchemy import and_

#internal
from model import Interval
from database import db

bp = Blueprint('main', __name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    app.register_blueprint(bp)
    return app

@bp.route('/intervals')
def get_intervals():
    day = request.args.get('day')
    query = db.session.query(Interval)
    if day is not None:
        started = datetime.strptime(day, '%Y-%m-%d')
        ended = started + timedelta(days=1)
        query = query.filter(and_(Interval.started >= started, Interval.ended <= ended))
    intervals = query.all()
    total_duration = sum((ivl.duration for ivl in intervals), timedelta())
    return render_template('intervals.html', 
        day=day,
        intervals=intervals,
        total_duration=total_duration
    )

@bp.route('/intervals/add', methods=['POST'])
def add_interval():
    data = request.get_json()
    started = iso8601.parse_date(
        data['started'],
        default_timezone=None
    )
    ended = iso8601.parse_date(
        data['ended'],
        default_timezone=None
    )

    interval = Interval(started=started, ended=ended)

    db.session.add(interval)
    db.session.commit()

    return jsonify({'status': 'ok'})
