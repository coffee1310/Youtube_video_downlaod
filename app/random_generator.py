import random
def random_personal_id():
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_'
    id_ = ''
    for i in range(1, random.randint(10,30)):
        id_ += (random.choice(chars))
    return id_
