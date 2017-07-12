'''
Created on 2017年7月11日

@author: Administrator
'''

import orm
from models import User,Blog,Comment
import asyncio





async def text(loop):
    loop = asyncio.get_event_loop()
    await orm.create_pool(loop=loop,user='root',password='123456',db='awesome')
    u = User(name='wangwu',email='wangwu123@126.com',passwd='123456',image='about:blank')
    await u.save()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(text(loop))
loop.close()