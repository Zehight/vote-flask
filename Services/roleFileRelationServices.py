# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, RoleFileRelation
from sqlalchemy import or_


def add(roleId, fileId,createBy):
    item = RoleFileRelation(
        roleId=roleId,
        fileId=fileId,
        createBy=createBy
    )
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList(roleId):
    result = db.session.query(RoleFileRelation).filter_by(roleId=roleId).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict
