import hashlib
import re


# def anonimyze(text):
#     identities = re.findall(r'\b\d{10}\b', text)
#
#     for identity in identities:
#         hashed_i = hashlib.sha1(identity.encode()).hexdigest()[-10:]
#         text = text.replace(identity, hashed_i)
#
#     return text

def hash(match):
    identity = match.group()
    hashed_i = hashlib.sha1(identity.encode()).hexdigest()[-10:]
    return hashed_i

def anonimyze(text):
    result = re.sub(r'\b\d{10}\b', hash, text)
    return result

text = 'Иван Драганов, ЕГН 9903142412 от град Пловдив'
print(anonimyze(text))
