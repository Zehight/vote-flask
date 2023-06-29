# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Role, RoleFileRelation
from sqlalchemy import or_


def add(name, createBy, code='', zone='', official='', originalName='', frontImg='', parentOfficial=''):
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
            createBy='test'
        )
        db.session.add(roleFileItem)
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList():
    result = db.session.query(Role).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict


def getInfo(id):
    result = db.session.query(Role).get(id)
    if result:
        result_dict = result.to_dict()
        frontImgResult = db.session.query(RoleFileRelation.fileId).filter_by(roleId=id).all()
        if frontImgResult:
            frontImgs  = [item[0] for item in frontImgResult]
        else:
            frontImgs = []
        result_dict['frontImgs'] = frontImgs
        return result_dict
    else:
        return ''

def delInfo(id):
    result =  db.session.query(Role).get(id)
    db.session.delete(result)
    db.session.commit()
    return 'successful'

