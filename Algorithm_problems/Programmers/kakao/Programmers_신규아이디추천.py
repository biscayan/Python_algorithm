import re

def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # step 2
    new_id = re.sub('[^a-z0-9-_.]','',new_id)
    # step 3
    new_id = re.sub('[.]{2,}','.',new_id)
    # step 4
    if new_id[0] =='.' or new_id[-1] =='.':
        new_id = new_id.strip('.')
    # step 5
    if new_id == '':
        new_id += 'a'
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] =='.':
            new_id = new_id.strip('.')
    # step 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    return new_id