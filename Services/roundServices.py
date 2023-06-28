# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Round
from sqlalchemy import or_


def add(projectId, name, showTime, startVoteTIme, endVoteTime ,createBy,remark='',frontImg=''):
    item = Round(
        id=snowflake.generate_id(),
        name=name,
        projectId=projectId,
        showTime=showTime,
        startVoteTIme=startVoteTIme,
        endVoteTime=endVoteTime,
        frontImg=frontImg,
        remark=remark,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList(projectId):
    result = db.session.query(Round).filter_by(projectId=projectId).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict
