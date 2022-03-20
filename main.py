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
            embed = discord.Embed(title='Go to YouTube',
                                  url='https://www.youtube.com/',
                                  description='New video guys click on the title')
            await message.channel.send(embed=embed)

        if message.content.startswith('!inspire'):
            quote = oth.get_quote()
            await message.channel.send(quote)

        if message.content.startswith('!follow'):

            args = message.content.split(" ")
            nums = 5 if len(args) != 2 else int(args[1])
            pics = pix.get_following_works(nums)

            for embed in pics:
                await message.channel.send(embed=embed)


client = BaseClient()

# run client instance
client.run(os.getenv('TOKEN'))
