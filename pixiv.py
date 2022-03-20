import os
import sys
import requests
import settings
import io
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
    json_result = papi.illust_follow()
    return json_result


# get_following_works(10)
