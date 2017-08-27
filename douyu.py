#encoding:utf-8
from douyu.chat.room import ChatRoom
import time,os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def on_chat_message(msg):
	os.environ['TZ']='Asia/Shanghai'
	#time.tzset()
	msg_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	user = msg.attr('nn')
	txt = msg.attr('txt')
	level = msg.attr('level')
	print "[%s] [lv%s %s]:%s" % (msg_time,level,user,txt)

def run():
	room = ChatRoom(sys.argv[1])
	room.on('chatmsg', on_chat_message)
	room.knock()

if __name__ == '__main__':
	run()
