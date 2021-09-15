from aiohttp import web



@web.middleware
async def error_middleware(request, handler):
 pass