from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def to_dict_decorator(cls):
    def to_dict(self):
        def format_datetime(dt):
            return dt.strftime('%Y-%m-%d')

        return {
            prop: format_datetime(getattr(self, prop)) if isinstance(getattr(self, prop), datetime) else getattr(self,
                                                                                                                 prop)
            for prop in self.__dict__ if not prop.startswith('_')}

    cls.to_dict = to_dict
    return cls


@to_dict_decorator
class Project(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    frontImg = db.Column(db.String(255), nullable=False)
    remark = db.Column(db.String(255))
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255), nullable=False)


@to_dict_decorator
class Round(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    showTime = db.Column(db.DateTime)
    startVoteTime = db.Column(db.DateTime)
    endVoteTime = db.Column(db.DateTime)
    freezeType = db.Column(db.String(255))
    remark = db.Column(db.String(255))
    frontImg = db.Column(db.String(255), nullable=False)
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255), nullable=False)


@to_dict_decorator
class Group(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    roundId = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    voteNum = db.Column(db.Integer(), nullable=False)
    promotedNum = db.Column(db.Integer(), nullable=False)
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255), nullable=False)


@to_dict_decorator
class Role(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    code = db.Column(db.String(255))
    name = db.Column(db.String(255), nullable=False)
    originalName = db.Column(db.String(255))
    zone = db.Column(db.String(255))
    official = db.Column(db.String(255))
    parentOfficial = db.Column(db.String(255))
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255), nullable=False)


@to_dict_decorator
class File(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255), nullable=False)


@to_dict_decorator
class RoleFileRelation(db.Model):
    roleId = db.Column(db.String(255), primary_key=True)
    fileId = db.Column(db.String(255), primary_key=True)
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255), nullable=False)


@to_dict_decorator
class RoleHistaryRelation(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    roleId = db.Column(db.String(255))
    title = db.Column(db.String(255))
    describe = db.Column(db.String(255))
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255))


@to_dict_decorator
class GroupRoleRelation(db.Model):
    id = db.Column(db.String(255))
    groupId = db.Column(db.String(255), primary_key=True)
    roleId = db.Column(db.String(255), primary_key=True)
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createBy = db.Column(db.String(255))
