import logging
import requests
from aiogram import Bot,Dispatcher,types,executor


API_TOKEN='8161549736:AAFSh0toZ_sMczRic6ulMCaKOVeC0534ejA'
logging.basicConfig(level=logging.INFO)


bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)



# start komandasi uchun handler
@dp.message_handler(commands='start')
async  def start_handler(message:types.Message):
    username=message.from_user.full_name
    text=f"𝗔𝘀𝘀𝗮𝗹𝗼𝗺𝘂 𝗮𝗹𝗲𝘆𝗸𝘂𝗺 {username}\n\n"
    text+=f"𝗩𝗮𝗹𝘆𝘂𝘁𝗮 𝗸𝘂𝗿𝘀𝗹𝗮𝗿𝗶 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗯𝗼𝘁𝗶𝗴𝗮 𝘅𝘂𝘀𝗵 𝗸𝗲𝗹𝗶𝗯𝘀𝗶𝘇\n"
    text+=f"𝗩𝗮𝗹𝘆𝘂𝘁𝗮 𝗸𝘂𝗿𝘀𝗹𝗮𝗿𝗶𝗻𝗶 𝗯𝗶𝗹𝗶𝘀𝗵 𝘂𝗰𝗵𝘂𝗻 /valyuta 𝘆𝗼𝘇𝗶𝗻𝗴"
    await message.answer(text,parse_mode='Markdown')


@dp.message_handler(commands='valyuta')
async def valyuta_course(message:types.Message):
        request=requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        response=request.json()

        text=f"Sana: x{response[0]['Date']}\n\n"
        CURRENSY=['USD','EUR','RUB','EGP']

        for i in response:
            if i['Ccy'] in CURRENSY:
                text+=f"1 {i['CcyNm_UZC']} ~ {i['Rate']} so'm\n"
        await message.answer(text)





if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
