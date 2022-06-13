import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime
import noti as noty


def replyAptData(date_param, user, loc_param='11710'): 
    print(user, date_param, loc_param) 
    res_list = noty.getData( loc_param, date_param )
# 하나씩 보내면 메세지 개수가 너무 많아지므로
# 300자까지는 하나의 메세지로 묶어서 보내기. 
    msg = '' 
    for r in res_list: 
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noty.MAX_MSG_LENGTH: 
            noty.sendMessage( user, msg ) 
            msg = r+'\n' 
        else: msg += r+'\n'
    if msg: 
        noty.sendMessage( user, msg ) 
    else: 
        noty.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param)


def save( user, loc_param ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS \
         users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try: 
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param)) 
    except sqlite3.IntegrityError: 
        noty.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' ) 
        return
    else: 
        noty.sendMessage( user, '저장되었습니다.' )
        conn.commit()


def check( user ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, locationTEXT, PRIMARY KEY(user, location) )') 
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall(): 
        row = 'id:' + str(data[0]) + ', location:' + data[1] 
        noty.sendMessage( user, row )


def handle(msg): 
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text': 
        noty.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
        return
    text = msg['text'] 
    args = text.split(' ')
    if text.startswith('item'):
        pass 
    #     print('try to bsn_nm') 
    #     replyAptData( args[1], chat_id, args[2] ) 
    # elif text.startswith('지역') and len(args)>1: 
    #     print('try to 지역', args[1]) 
    #     replyAptData( '202205', chat_id, args[1] ) 
    # elif text.startswith('저장') and len(args)>1: 
    #     print('try to 저장', args[1]) 
    #     save( chat_id, args[1] )
    # elif text.startswith('확인'): 
    #     print('try to 확인') 
    #     check( chat_id ) 
    else: noty.sendMessage(chat_id, '''도움말.\n 사용가능 여부 [Y/N] \n 지역 [지역명] \n\
        지역 ["도화동,Y","숭의동,Y","주안동,Y","학익동,N","용현동,Y"]''')


today = date.today() 
current_month = today.strftime('%Y%m')
print( '[',today,']received token :', noty.TOKEN )
from noti import bot
pprint( bot.getMe() )
bot.message_loop(handle)
print('Listening...') 
while 1: 
    time.sleep(10)