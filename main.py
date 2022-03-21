import os
import requests
import json
import settings
from discord import *
import pixiv as pix
import other as oth


class BaseClient(Client):

    async def on_ready(self):
        pix.init()
        print('I have logged in as {0.user}'.format(self))
        # print(os.getenv('refresh_token'))

    async def on_message(self, message: Message):
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

    async def on_reaction_add(self, reaction: Reaction, user: User):

        if reaction.message.author == self.user and user != self.user:
            if str(reaction.emoji) == '🔽':
                await reaction.message.add_reaction('👍')
                # TODO: NAME CONFLICTION AND DOWNLOAD LOCATION
                for embed in reaction.message.embeds:
                    if embed.image.url.endswith('jpg'):
                        pic = open(embed.title + str('.jpg'), 'wb')
                    elif embed.image.url.endswith('png'):
                        pic = open(embed.title + str('.png'), 'wb')
                    elif embed.image.url.endswith('gif'):
                        pic = open(embed.title + str('.gif'), 'wb')
                    pic.write(requests.get(embed.image.url).content)
                    pic.close()
                await reaction.message.remove_reaction(reaction, user)


client = BaseClient()

# run client instance
client.run(os.getenv('TOKEN'))
