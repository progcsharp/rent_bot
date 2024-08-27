from db import make_session, ModerTgUser


async def update_user_by_password(password, name, lower_name):
    session = make_session()
    user = session.query(ModerTgUser).filter(ModerTgUser.password == password).first()
    user.name = name
    user.lower_name = lower_name
    session.add(user)
    session.commit()
    session.close()
    return user


async def update_user_tg_id(password, tg_id):
    session = make_session()
    user = session.query(ModerTgUser).filter(ModerTgUser.password == password).first()
    user.tg_id = tg_id
    session.add(user)
    session.commit()
    session.close()
    return user


async def update_user_card(tg_id, card):
    session = make_session()
    user = session.query(ModerTgUser).filter(ModerTgUser.tg_id == tg_id).first()
    user.cart = card
    session.add(user)
    session.commit()
    session.close()
    return user
