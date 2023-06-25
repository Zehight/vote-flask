# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Project
from sqlalchemy import or_


def add(name, startTime, endTime, frontImg, remark, createBy):
    item = Project(
        id=snowflake.generate_id(),
        name=name,
        startTime=startTime,
        endTime=endTime,
        frontImg=frontImg,
        remark=remark,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList():
    result = db.session.query(Project).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict
