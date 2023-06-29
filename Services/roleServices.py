# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Role, RoleFileRelation
from sqlalchemy import or_


def add(name, createBy,code, zone='', official='', originalName='', frontImg='',parentOfficial=''):
    id = snowflake.generate_id()
    item = Role(
        id=id,
        code=code,
        name=name,
        originalName=originalName,
        zone=zone,
        official=official,
        createBy=createBy,
        parentOfficial=parentOfficial
    )
    if frontImg != '':
        roleFileItem = RoleFileRelation(
            fileId=frontImg,
            roleId=id,
            createBy = 'test'
        )
        db.session.add(roleFileItem)
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList():
    result = db.session.query(Role).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict

def getInfo(roleId):
    result = db.session.query(Role).get(roleId)
    result_dict = result.to_dict()
    return result_dict
