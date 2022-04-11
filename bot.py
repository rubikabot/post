from requests import get
from re import findall
from rubika.client import Bot
import time

bot = Bot("AppName", auth="sduqfyoqcdicecmhrcrrivqusijxqiot")


while True:
	
	time.sleep(5)
	x = get("https://api.codebazan.ir/jok/").text
	cp = f" Xp Post Gozar :) \n @post_xp"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("g0BcYEq00e3179342e80c96d465db2d8", jok)
	print('sended')
