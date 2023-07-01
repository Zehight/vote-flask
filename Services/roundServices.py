# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Round
from .groupServices import getList as GroupGetList
from sqlalchemy import or_


def add(projectId, name, showTime, startVoteTime, endVoteTime, createBy, remark='', frontImg='', freezeType=0):
    id = snowflake.generate_id()
    item = Round(
        id=id,
        name=name,
        projectId=projectId,
        showTime=showTime,
        startVoteTime=startVoteTime,
        endVoteTime=endVoteTime,
        frontImg=frontImg,
        remark=remark,
        freezeType=freezeType,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return id


def getList(projectId):
    result = db.session.query(Round).filter_by(projectId=projectId).all()
    if result:
        result_dict = [round.to_dict() for round in result]
        return result_dict
    else:
        return []


def getInfo(id):
    result = db.session.query(Round).get(id)
    if result:
        result_dict = result.to_dict()
        groupList = GroupGetList(id)
        result_dict['groupList'] = groupList
        return result_dict
    else:
        return ''

def delInfo(id):
    result = db.session.query(Round).get(id)
    db.session.delete(result)
    return 'successful'
