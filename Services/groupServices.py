# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, Group
from sqlalchemy import or_


def add(RoundId, name, voteNum, promotedNum, createBy):
    item = Group(
        RoundId=RoundId,
        id=snowflake.generate_id(),
        name=name,
        voteNum=voteNum,
        promotedNum=promotedNum,
        createBy=createBy,
    )
    db.session.add(item)
    db.session.commit()
    return 'successful'


def getList(RoundId):
    result = db.session.query(Group).filter_by(RoundId=RoundId).all()
    result_dict = [project.to_dict() for project in result]
    return result_dict
