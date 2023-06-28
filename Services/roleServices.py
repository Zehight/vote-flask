# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Role
from sqlalchemy import or_


def add(name,createBy, zone='', official='', originalName='',):
    item = Role(
        id=snowflake.generate_id(),
        name=name,
        originalName=originalName,
        zone=zone,
        official=official,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList():
    result = db.session.query(Role).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict
