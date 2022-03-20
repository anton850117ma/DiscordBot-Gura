import os
import sys
import requests
import settings
import io
import discord
from datetime import datetime
from pixivpy3 import *
# import aiohttp
# import asyncio
# from pixivpy_async import *

if sys.version_info >= (3, 0):
    import importlib
    importlib.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

# filename = url[url.rindex('.'):]
# async with aiohttp.ClientSession() as session:
#     async with session.get(url) as resp:
#         data = io.BytesIO(await resp.read())
#         await message.channel.send(file=discord.File(data, illust.title + filename))


def init():

    api = AppPixivAPI()
    api.auth(refresh_token=os.getenv('refresh_token'))
    return api


def get_following_works(nums):

    papi = init()
    data = papi.illust_follow()
    pics = []
    for index in range(nums):
        illust = data.illusts[index]
        if len(illust['meta_single_page']) > 0:
            embed = discord.Embed(
                title=illust['title'], color=3447003)
            embed.set_image(url=illust.meta_single_page['original_image_url'].replace(
                'i.pximg.net', 'i.pixiv.cat'))
            embed.set_author(
                name=illust.user['name'],
                icon_url=illust.user.profile_image_urls['medium'].replace(
                    'i.pximg.net', 'i.pixiv.cat'))
            embed.set_footer(text=illust['create_date'])
            pics.append(embed)
        else:
            for pic in illust['meta_pages']:
                embed = discord.Embed(
                    title=illust['title'], color=10181046)
                embed.set_image(url=pic.image_urls['original'].replace(
                    'i.pximg.net', 'i.pixiv.cat'))
                embed.set_author(
                    name=illust.user['name'],
                    icon_url=illust.user.profile_image_urls['medium'].replace(
                        'i.pximg.net', 'i.pixiv.cat'))
                embed.set_footer(text=illust['create_date'])
                pics.append(embed)
    return pics
