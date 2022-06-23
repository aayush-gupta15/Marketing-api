from db import db


class FacebookModel(db.Model):
    __tablename__ = 'Facebook_campaign'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    impressions = db.Column(db.Integer)
    spend = db.Column(db.Integer)
    clicks = db.Column(db.Integer)
    reach = db.Column(db.Integer)
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    conversions = db.Column(db.Integer)


    def __init__(self, name, impressions, spend, clicks, reach, startDate, endDate, conversions):
        self.name = name
        self.impressions = impressions
        self.spend = spend
        self.clicks = clicks
        self.reach = reach
        self.startDate = startDate
        self.endDate = endDate
        self.conversions = conversions

    def json(self):
        return {'name': self.name, 'impressions': self.impressions, 'spend': self.spend, 'clicks': self.clicks,
                'reach': self.reach, 'startDate': self.startDate, 'endDate': self.endDate, 'conversion': self.conversions}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()