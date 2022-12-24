
import dgram
from dgram.async_dgram import Asyncdgram


import logging

logger = dgram.logger
dgram.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

class ExceptionHandler(dgram.ExceptionHandler):
    def handle(self, exception):
        logger.error(exception)

bot = Asyncdgram('TOKEN',exception_handler=ExceptionHandler())




@bot.message_handler(commands=['photo'])
async def photo_send(message: dgram.types.Message):
    await bot.send_message(message.chat.id, 'Hi, this is an example of exception handlers.')
    raise Exception('test') # Exception goes to ExceptionHandler if it is set
    


import asyncio
asyncio.run(bot.polling())
