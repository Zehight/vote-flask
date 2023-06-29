# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Group
from .groupRoleRelationServices import getInfo as roleInGroupGetInfo
from sqlalchemy import or_


def add(roundId, name, voteNum, promotedNum, createBy):
    id = snowflake.generate_id()
    item = Group(
        roundId=roundId,
        id=id,
        name=name,
        voteNum=voteNum,
        promotedNum=promotedNum,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return id


def getList(roundId):
    result = db.session.query(Group).filter_by(roundId=roundId).all()
    if result:
        result_dict = [group.to_dict() for group in result]
        for item in result_dict:
            groupRoleInfo = roleInGroupGetInfo(item['id'])
            item['roleList'] = groupRoleInfo
        return result_dict
    else:
        return []


def getInfo(id):
    result = db.session.query(Group).get(id)
    if (result):
        result_dict = result.to_dict()
        groupRoleInfo = roleInGroupGetInfo(id)
        result_dict['roleList'] = groupRoleInfo
        return result_dict
    else:
        return ''


def delInfo(id):
    result = db.session.query(Group).get(id)
    db.session.delete(result)
    db.session.commit()
    return 'successful'
