import os
import discord
import requests
import json
import settings
import pixiv as pix
import other as oth


class BaseClient(discord.Client):

    async def on_ready(self):
        print('I have logged in as {0.user}'.format(self))
        # print(os.getenv('refresh_token'))

    async def on_message(self, message):
        if message.author == self.user:
            return

        # hellow world!
        if message.content.startswith('!hello'):
            await message.channel.send("Hello World!")

        # make inspire
        if message.content.startswith('!inspire'):
            quote = oth.get_quote()
            await message.channel.send(quote)

        # show several artworks
        if message.content.startswith('!follow'):
            args = message.content.split(" ")
            nums = 5 if len(args) != 2 else int(args[1])
            pics = pix.get_following_works(nums)
            for embed in pics:
                msg = await message.channel.send(embed=embed)
                await msg.add_reaction('🔽')


client = BaseClient()

# run client instance
client.run(os.getenv('TOKEN'))
