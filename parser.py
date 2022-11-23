import re

class Event:
    def __init__(self, tilte, date, time, location, description):
        self.title = tilte
        self.date = date
        self.time = time
        self.location = location
        self.description = description
    
    def __str__():
        string = self.title + '\n'
        string += str(self.date) + '\n'
        string += str(self.time) + '\n'
        string += self.location + '\n'
        string += self.description + '\n'
        return string

def split_query(query:str) -> list:
    # 複数の区切りによる文字列の分割
    return re.split(' 　-~ー〜', query)
    
def check_date(word:str) -> bool:
    # 数字以外の日付として有効な文字
    valid_char_list = list('/／月火水木金土日()（）')
    # 各文字が日付として有効なものか
    check = False
    for char in word:
        # 文字が10進数の数字であるか(全角数字を含む)
        if char.isdecimal():
            continue
        # 文字がvalid_char_listに含まれる文字であるか
        if char in valid_char_list:
            check = True
            continue
        return False
    return True and check
        
def check_time(word:str) -> bool:
    # 数字以外の時間として有効な文字
    valid_char_list = list(':：時分秒半正午前後')
    # 各文字が時間として有効なものか
    for char in word:
        # 文字が10進数の数字であるか(全角数字を含む)
        if char.isdecimal():
            continue
        # 文字がvalid_char_listに含まれる文字であるか
        if char in valid_char_list:
            continue
        return False
    return True

def all_check_status(word:str) -> str:
    status = 'date:{},'.format(check_date(word))
    status += 'time:{},'.format(check_time(word))
    return status

query = '12/1 14:00 shopping'
words = query.split()

title, date, time = [], [], []

for word in words:
    if check_date(word):
        date.append(word)
    elif check_time(word):
        time.append(word)
    else:
        title.append(word)

print('title:{}'.format(title))
print('date:{}'.format(date))
print('time:{}'.format(time))