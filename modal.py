from peewee import *
from datetime import datetime

database = MySQLDatabase('douyindb', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
                                        'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'gxz153759'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database

def getTimeStampStr():
    # current date and time
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return int(str(timestamp).replace('.', ''))


# User
class ComUser(BaseModel):
    tags = CharField()
    user_name = CharField() # 抖音名称
    user_id = CharField()
    user_url = CharField()
    real_url = CharField()
    v_uri = CharField()
    v_size = IntegerField(default=0)
    desc = CharField()
    isupload = BooleanField(default=False)
    c_date = BigIntegerField(default=getTimeStampStr())

    class Meta:
        table_name = 'com_user'


# challenge
class ComChallenge(BaseModel):

    class Meta:
        table_name = 'com_challenge'


# music
class ComMusic(BaseModel):

    class Meta:
        table_name = 'com_music'

if __name__ == "__main__":
    ComUser.create_table()
    ComUser(user_id="xxx", user_url="xx", user_name="xxx").save()