import os
import sys
import requests
import settings
import io
from discord import Embed
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
papi = None

def init():
    global papi
    papi = AppPixivAPI()
    papi.auth(refresh_token=os.getenv('refresh_token'))


def replace_url(url):
    return url.replace('i.pximg.net', 'i.pixiv.cat')


def get_following_works(nums):
    global papi
    data = papi.illust_follow()
    pics = []
    for index in range(nums):
        illust = data.illusts[index]
        if len(illust['meta_single_page']) > 0:
            # TODO: URL=ORIGINAL, IMAGE_URL=LARGE
            embed = Embed(
                title=illust['title'], url='', color=3447003)
            embed.set_image(url=replace_url(
                illust.meta_single_page['original_image_url']))
            embed.set_author(
                name=illust.user['name'],
                icon_url=replace_url(illust.user.profile_image_urls['medium']))
            embed.set_footer(text=illust['create_date'])
            pics.append(embed)
        else:
            for pic in illust['meta_pages']:
                embed = Embed(
                    title=illust['title'], color=10181046)
                embed.set_image(url=replace_url(pic.image_urls['original']))
                embed.set_author(
                    name=illust.user['name'],
                    icon_url=replace_url(illust.user.profile_image_urls['medium']))
                embed.set_footer(text=illust['create_date'])
                pics.append(embed)
    return pics
