from dgram.async_dgram import Asyncdgram

import dgram
bot = Asyncdgram('TOKEN')

@bot.chat_join_request_handler()
async def make_some(message: dgram.types.ChatJoinRequest):
    await bot.send_message(message.chat.id, 'I accepted a new user!')
    await bot.approve_chat_join_request(message.chat.id, message.from_user.id)

import asyncio
asyncio.run(bot.polling())