from aiogram import types
from aiogram.utils import executor
from loader import dp, db, bot
from pathlib import Path
from aiogram.types import ContentType, File, Message
from datetime import datetime
import speech_recognition as sr

import subprocess
import os






admin_id = [622550539]
r = sr.Recognizer()



@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = "files/voices"
    file_name_ogg = f"{voice.file_id}.ogg"
    file_name_wav = f"{voice.file_id}.wav"

    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    await bot.download_file(file_path=voice.file_path, destination=f"{path}/{file_name_ogg}")

    process = subprocess.run(['ffmpeg', '-i', f"{path}/{file_name_ogg}", f"{path}/{file_name_wav}"])
    os.remove(f"{path}/{file_name_ogg}")

    with sr.AudioFile(f"{path}/{file_name_wav}") as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="ru-RU")
    await message.reply(text)
    await message.answer('prinver')

    







# @dp.message_handler(content_types=[ContentType.VOICE])
# async def voice_message_handler(message: types.Message):

#     voice = await message.voice.get_file()
#     path = "voices"
#     date = datetime.now()
#     file_name = f'{voice.file_id}.ogg'
#     userid = message.from_user.id
#     username = message.from_user.username
#     info = db.add_name(userid=userid, voice_name=file_name, username=username, date=date)

#     Path(f"{path}").mkdir(parents=True, exist_ok=True)
#     await bot.download_file(file_path=voice.file_path, destination=f"{path}/{file_name}")

#     filename = db.select_voice()

#     file_name_ogg = f"{voice.file_id}.ogg"
#     file_name_wav = f"{voice.file_id}.wav"

    
#     process = subprocess.run(['ffmpeg', '-i', f"{path}/{file_name_ogg}", f"{path}/{file_name_wav}"])
#     os.remove(f"{path}/{file_name_ogg}")

#     with sr.AudioFile(f"{path}/{file_name_wav}") as source:
#         audio_data = r.record(source)
#         text = r.recognize_google(audio_data)
#     await message.reply(text)
    

#     # with sr.AudioFile(f"voices/output2.wav") as source:
#     #     # listen for the data (load audio to memory)
#     #     audio_data = r.record(source)
#     #     # recognize (convert from speech to text)
#     #     text = r.recognize_google(audio_data)
#     # await message.reply(text)


    
    

# if __name__ == '__main__':
#     executor.start_polling(dp)
