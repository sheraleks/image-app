from aiohttp import web


# TODO: обработка ошибок
@web.middleware
async def error_middleware(request, handler):
 pass