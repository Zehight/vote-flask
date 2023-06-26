# 雪花ID
from snowflake import Snowflake
from datetime import datetime

snowflake = Snowflake(0, 0, 0, datetime(2023, 1, 1))

# 数据库相关
from models import db, connect_db, File
from sqlalchemy import or_


def add(name):
    id = snowflake.generate_id(),
    item = File(
        id=id,
        name=name,
        createBy='test'
    )
    db.session.add(item)
    db.session.commit()
    return id


