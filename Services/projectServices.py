# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Project, Round, Group, Role, GroupRoleRelation, RoleFileRelation
from .roundServices import getList as RoundGetList
from sqlalchemy import or_


def add(name, startTime, endTime, frontImg, remark, createBy):
    id = snowflake.generate_id()
    item = Project(
        id=id,
        name=name,
        startTime=startTime,
        endTime=endTime,
        frontImg=frontImg,
        remark=remark,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return id


def getList():
    result = db.session.query(Project).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict


def getInfo(id):
    result = db.session.query(Project).get(id)
    if result:
        projectInfo = result.to_dict()
        roundList = RoundGetList(id)
        projectInfo['roundList'] = roundList
        return projectInfo
    else:
        return ''


def delInfo(id):
    result = db.session.query(Project).get(id)
    db.session.delete(result)
    db.session.commit()
    return 'successful'
