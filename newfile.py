from rubpy import WebSocket, Client
from asyncio import run
from urllib import request
from requests import get
import os
	
auth: str = 'vkbusiuotdwxvkobowrgrihrdcxqhyox'
bot = WebSocket(auth)
app = Client(auth)

async def main():
    async for message in bot.handler():
        message_type: str = message.get('message').get('type')
        text: str = message.get('message')
        object_guid: str = message.get('object_guid')
        message_id: str = message.get('message_id')
       
        if text.get('text') == '/start':
            try:
           	 username:dict = await app.getUserInfo(text['author_object_guid'])
           	 username : str = username['data']['user']['first_name']
           	 await app.sendMessage(object_guid , f"سلام **{username}** عزیز به ربات اینستا گرام دانلودر خوش آمدی 🗿❤️ برای دانلود پست مورد نظرت دستور زیرو ارسال کن:\nدانلود link post\n\n!!!توجه داشته باشید جای link post لینک پست مورد نظرتو بزارید." , reply_to_message_id=message_id)
            except:pass
        
        elif message_type == 'Text':
        	try:
        		msg: str = message.get('message').get('text')
        		if msg.startswith('دانلود'):
        			urls:str = msg.replace('دانلود ','')
        			response:dict = get('https://api.irateam.ir/insta2.php?type=post&url=' + urls).json()
        			url:str = response['Results'][0]['post']
        			print(url)
        			name = 'Video.mp4'
        			print('لینک دریافت شد ...')
        			try:
        				request.urlretrieve(url, name)
        				print('فایل دریافت شد ...')
        			except: pass
        			t: bool = False
        			while(t !=True):
        				try:
        					await app.sendVideo(object_guid, name,caption='پست مورد نظر شما!\n\nBOT : @MMD_bot_jr1', reply_to_message_id=message_id)
        					print('فایل ارسال شد.')
        					t: bool = True
        				except:
        					t: bool = False
        	except:pass
        			
run(main())