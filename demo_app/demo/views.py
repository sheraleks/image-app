import aiohttp
import aiohttp_jinja2
from aiohttp.web_request import Request
from aiohttp.web_urldispatcher import View

from image_app.config import config


class BlackWhiteView(View):
    @aiohttp_jinja2.template("index.html")
    async def get(self):
        return {
            "title": "Black or white pixels",
            "upload_route": "/black_white",
            "port": config["server"]["port"],
        }

    @aiohttp_jinja2.template("index.html")
    async def post(self):
        data = await self.request.post()
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                f"http://0.0.0.0:{config['server']['port']}/api/black_white",
                data={
                    "image": getattr(data["image"], "file", None)
                })
        response_body = await response.json()
        status = response_body["status"]
        result = f"Major pixel color is {response_body['data']['major_color']}" if status == "ok" else response_body
        return {
            "title": "Black or white pixels",
            "upload_route": "/black_white",
            "port": config["server"]["port"],
            "result": result,
        }
