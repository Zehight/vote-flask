# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Role, RoleFileRelation, GroupRoleRelation

from .roleServices import getInfo as roleGetInfo


def add(roleId, groupId, createBy):
    id = snowflake.generate_id()
    item = GroupRoleRelation(
        id=id,
        roleId=roleId,
        groupId=groupId,
        createBy=createBy
    )
    db.session.add(item)
    db.session.commit()
    return id


def getInfo(groupId):
    roleList = []
    result = db.session.query(GroupRoleRelation).filter_by(groupId=groupId).all()
    if result:
        result_dict = [item.to_dict() for item in result]
        for item in result_dict:
            roleItem = roleGetInfo(item['roleId'])
            roleList.append(roleItem)
    return roleList


def delInfo(groupId,roleId):
    result = db.session.query(GroupRoleRelation).get((groupId,roleId))
    db.session.delete(result)
    db.session.commit()
    return 'successful'
