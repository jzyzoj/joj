from joj import Session
import time

def Check_privilege(user,pri):
    return (user.privileges & (1<<pri))==1

def Get_cur_time(flag=False):
    if Flag=False:
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    else:
        return time.time()

def Update(example):
    try:
        session=Session()
        session.commit()

    except :
        session.rollback()

    finally:
        session.close()

def Add(example):
    try:
        session=Session()
        session.add(example)
        session.commit()

    except :
        session.rollback()

    finally:
        session.close()

def Delete(example):
    try:
        session=Session()
        session.delete(example)
        session.commit()

    except :
        session.close()

    finally:
        session.close()

