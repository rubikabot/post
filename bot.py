from requests import get
from re import findall
from rubika.client import Bot
import time

bot = Bot("AppName", auth="sduqfyoqcdicecmhrcrrivqusijxqiot")


while True:
	
	time.sleep(60)
	x = get("https://api.codebazan.ir/jok/").text
	cp = f" BOT BLACK STAR:) \n @bot_jok"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("c0BEYfz038812475acf56417765cd08d", jok)
	print('sended')
