import os
import discord
import requests
import json
import settings
import pixiv as pix
import other as oth


class BaseClient(discord.Client):

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
        # print(os.getenv('refresh_token'))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('!follow'):

            args = message.content.split(" ")
            nums = 5 if len(args) != 2 else int(args[1])
            data = pix.get_following_works(nums)

            for index in range(nums):
                illust = data.response[index]
                url = illust.image_urls['large'].replace(
                    'i.pximg.net', 'i.pixiv.cat')

                my_string = str(index+1) + ". " + url
                await message.channel.send(my_string)

        if message.content.startswith('!inspire'):
            quote = oth.get_quote()
            await message.channel.send(quote)


client = BaseClient()

# run client instance
client.run(os.getenv('TOKEN'))
