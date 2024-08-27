from db import make_session, ModerTgUser, Info, Moder, Message


async def get_user_by_tg_id(tg_ig):
    session = make_session()
    user = session.query(ModerTgUser).filter(ModerTgUser.tg_id == tg_ig).first()
    session.close()
    if user:
        return False
    return True


async def get_user_by_password(password):
    session = make_session()
    user = session.query(ModerTgUser).filter(ModerTgUser.password == password).first()
    session.close()
    if user:
        return True
    return False


async def get_user(tg_id):
    session = make_session()
    user = session.query(ModerTgUser).filter(ModerTgUser.tg_id == tg_id).first()
    session.close()
    return user


async def get_info():
    session = make_session()
    info = session.query(Info).filter(Info.id == 1).first()
    session.close()
    return info


async def get_moder():
    session = make_session()
    moder = session.query(Moder).filter(Moder.id == 1).first()
    session.close()
    return moder.tg_id


async def get_message(mess_name):
    session = make_session()
    message = session.query(Message).filter(Message.name==mess_name).first()
    session.close()
    return message.message
