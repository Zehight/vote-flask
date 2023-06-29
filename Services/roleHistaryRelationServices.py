# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, RoleHistaryRelation
from sqlalchemy import or_


def add(roleId, title, describe, createBy):
    id = snowflake.generate_id()
    item = RoleHistaryRelation(
        id=id,
        roleId=roleId,
        title=title,
        describe=describe,
        createBy=createBy
    )
    db.session.add(item)
    db.session.commit()
    return id


def getList(roleId):
    result = db.session.query(RoleHistaryRelation).filter_by(roleId=roleId).all()
    if result:
        result_dict = [item.to_dict() for item in result]
        return result_dict
    else:
        return []


def getInfo(id):
    result = db.session.query(RoleHistaryRelation).get(id)
    if result:
        result_dict = result.to_dict()
        return result_dict
    else:
        return ''


def delInfo(id):
    result = db.session.query(RoleHistaryRelation).get(id)
    db.session.delete(result)
    return 'successful'
